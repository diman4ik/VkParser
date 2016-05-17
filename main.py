import os
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
    return api.get('users.search', city=pcity, count=2, fields='first_name,last_name, sex')
    
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    
    if not os.path.isfile("music.db"):
        songdb.createDB()
    
    login, password = showLoginDialog()
    
    (stoken,user_id) = vk_auth.auth(login, password, '5466274', 'audio')
    
    QtGui.QMessageBox.about(QtGui.QWidget(), "Супер токен", stoken)
    
    vk = vkontakte.API(token=stoken)
    
    users = getUsersFromCity(vk, 157)
    
    print(users)
    
    Dialog = QtGui.QDialog()
    ui = main_form.Ui_Dialog()
    ui.setupUi(Dialog)
    
    ui.peopleFilterButton.clicked.connect(refreshClicked)
	
    Dialog.show()
    sys.exit(app.exec_())
