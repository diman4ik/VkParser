import http.cookiejar
import urllib
from urllib.parse import urlparse
from html.parser import HTMLParser

class FormParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.url = None
        self.params = {}
        self.in_form = False
        self.form_parsed = False
        self.method = "GET"

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        if tag == "form":
            if self.form_parsed:
                raise RuntimeError("Second form on page")
            if self.in_form:
                raise RuntimeError("Already in form")
            self.in_form = True 
        if not self.in_form:
            return
        attrs = dict((name.lower(), value) for name, value in attrs)
        if tag == "form":
            self.url = attrs["action"] 
            if "method" in attrs:
                self.method = attrs["method"]
        elif tag == "input" and "type" in attrs and "name" in attrs:
            if attrs["type"] in ["hidden", "text", "password"]:
                self.params[attrs["name"]] = attrs["value"] if "value" in attrs else ""

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag == "form":
            if not self.in_form:
                raise RuntimeError("Unexpected end of <form>")
            self.in_form = False
            self.form_parsed = True

def auth_user(email, password, client_id, scope, opener):
    response = opener.open(
        "http://oauth.vk.com/oauth/authorize?" + \
        "redirect_uri=http://oauth.vk.com/blank.html&response_type=token&" + \
        "client_id=%s&scope=%s&display=wap" % (client_id, ",".join(scope))
        )
    doc = str(response.read())
    parser = FormParser()
    parser.feed(doc)
    parser.close()
    if not parser.form_parsed or parser.url is None or "pass" not in parser.params or \
      "email" not in parser.params:
          raise RuntimeError("Something wrong")
    parser.params["email"] = email
    parser.params["pass"] = password
    
    params = urllib.parse.urlencode(parser.params)
    params = params.encode('utf-8')
    
    if parser.method == "post":
        response = opener.open(parser.url, params)
    else:
        raise NotImplementedError("Method '%s'" % parser.method)
    return response.read(), response.geturl()

def give_access(doc, opener):
    parser = FormParser()
    parser.feed(str(doc))
    parser.close()
    if not parser.form_parsed or parser.url is None:
          raise RuntimeError("Something wrong")
          
    params = urllib.parse.urlencode(parser.params)
    params = params.encode('utf-8')
          
    if parser.method == "post":
        response = opener.open(parser.url, params)
    else:
        raise NotImplementedError("Method '%s'" % parser.method)
    return response.geturl()


def auth(email, password, client_id, scope):
    if not isinstance(scope, list):
        scope = [scope]
    opener = urllib.request.build_opener(
        urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()),
        urllib.request.HTTPRedirectHandler())
    doc, url = auth_user(email, password, client_id, scope, opener)
    
    if urlparse(url).path != "/blank.html":
        # Need to give access to requested scope
        url = give_access(doc, opener)
    if urlparse(url).path != "/blank.html":
        raise RuntimeError("Expected success here "+urlparse(url).path)

    def split_key_value(kv_pair):
        kv = kv_pair.split("=")
        return kv[0], kv[1]

    answer = dict(split_key_value(kv_pair) for kv_pair in urlparse(url).fragment.split("&"))
    if "access_token" not in answer or "user_id" not in answer:
        raise RuntimeError("Missing some values in answer")
    return answer["access_token"], answer["user_id"] 
