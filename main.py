import os
import time
import json
from PyQt4 import QtCore, QtGui
import main_form
import songdb
import login_dialog
import filter
import vk_auth
import vk

def refreshClicked():
    Dialog = QtGui.QDialog()
    ui = filter.Ui_Dialog()
    ui.setupUi(Dialog)
    
    #Dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
    result = Dialog.exec_()
    
    if result == QtGui.QDialog.Accepted:
        city = ui.cityEdit.text()
        age_from = ui.spinBoxAgeFrom.text()
        age_to = ui.spinBoxAgeTo.text()
        QtGui.QMessageBox.about(QtGui.QWidget(), "Супер прога", city)
        return city, age_from, age_to
     
    return None
    
def showLoginDialog():
    Dialog = QtGui.QDialog()
    ui = login_dialog.Ui_Dialog()
    ui.setupUi(Dialog)
    
    result = Dialog.exec_()
    
    if result == QtGui.QDialog.Accepted:
        loginText =  ui.loginEdit.text()
        passwordText = ui.passwordEdit.text()
        return loginText, passwordText

    return None
    
def getUsersFromCity(api, pcity):
    # 365 запросов по всем дням в году - так преодолемм ограничение не больше 1000
    users = []
    
    request_count = 0 # не более 3 в секунду, делаем два и ждем пару сек
    
    for m in range(1, 13): # месяцы
        for d in range(1, 32): #дни
            result = api.users.search(city=pcity, birth_day=d, birth_month=m, count=2, fields='first_name,last_name, sex, bdate')
            
            result = json.loads(result)
            
            print(result)
        
            users.append()
            
            if request_count == 2:
                time.sleep(2)
                request_count = 0
            
            request_count += 1
            
    return users 
    
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    
    if not os.path.isfile("music.db"):
        songdb.createDB()
    
    login, password = showLoginDialog()
    
    (stoken,user_id) = vk_auth.auth(login, password, '5466274', 'audio')
    
    #QtGui.QMessageBox.about(QtGui.QWidget(), "Супер токен", stoken)
    
    #auth_session = vk.AuthSession(app_id='5466274', user_login=login, user_password=password)
    #stoken, _ = auth_session.get_access_token()

    session = vk.Session(access_token=stoken)
    vkapi = vk.API(session, lang='ru')
    
    users = getUsersFromCity(vkapi, 157)
    
    #print(users)
    
    Dialog = QtGui.QDialog()
    ui = main_form.Ui_Dialog()
    ui.setupUi(Dialog)
    
    ui.peopleFilterButton.clicked.connect(refreshClicked)
	
    Dialog.show()
    sys.exit(app.exec_())
