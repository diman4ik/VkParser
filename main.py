# -*- coding: utf8 -*-
import os
import time
import json
from PyQt4 import QtCore, QtGui, QtSql
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
    
progress = None
    
def enableAllControls(enable):
    return False
    
def createProgress(dialog):
    progress = QtGui.QProgressBar(dialog)
    progress.setGeometry(200, 80, 250, 20)
    progress.move(450, 400)
    progress.setValue(50)
    
def getUsersFromCity(api, pcity):
    # 365 запросов по всем дням в году - так преодолемм ограничение не больше 1000    
    request_count = 0 # не более 3 в секунду, делаем два и ждем пару сек
    
    for m in range(1, 4): # месяцы
        for d in range(1, 4): #дни
            tot_count=3
            result = api.users.search(city=pcity, birth_day=d, birth_month=m, count=tot_count, fields='sex, bdate')
            
            #result = json.loads(result)
            print(result)
            
            for ind in range(1, len(result)):
                age = 0
            
                if 'bdate' in result[ind]:
                    strage = result[ind]['bdate'].split('.')[-1]
                    
                    if len(strage) == 4:
                        age = 2016 - int(strage)
            
                songdb.addUser(result[ind]['uid'], result[ind]['first_name'], result[ind]['last_name'], result[ind]['sex'], pcity, age)
        
            if request_count == 2:
                time.sleep(2)
                request_count = 0
            
            request_count += 1
    
    print("info added")
    
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    
    if not os.path.isfile("music.db"):
        db = songdb.createDB()
    else:
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('music.db')
        
    if db is None or not db.open():
        QtGui.QMessageBox.critical(None, QtGui.qApp.tr("Cannot open database"),
            QtGui.qApp.tr("Unable to establish a database connection.\n"
            "This example needs SQLite support. Please read "
            "the Qt SQL driver documentation for information "
            "how to build it.\n\n" "Click Cancel to exit."),
            QtGui.QMessageBox.Cancel)
    else:
        login, password = showLoginDialog()
        
        (stoken,user_id) = vk_auth.auth(login, password, '5466274', 'audio')
        
        #QtGui.QMessageBox.about(QtGui.QWidget(), "Супер токен", stoken)
        
        #auth_session = vk.AuthSession(app_id='5466274', user_login=login, user_password=password)
        #stoken, _ = auth_session.get_access_token()
        
        print(stoken)

        session = vk.Session(access_token=stoken)
        vkapi = vk.API(session, lang='ru')
        
        #getUsersFromCity(vkapi, 157)
        count = songdb.getUsersCount()
        print(count)
    
    Dialog = QtGui.QDialog()
    ui = main_form.Ui_Dialog()
    ui.setupUi(Dialog)
    
    createProgress(Dialog)
    
    ui.peopleFilterButton.clicked.connect(refreshClicked)
	
    Dialog.show()
    sys.exit(app.exec_())
