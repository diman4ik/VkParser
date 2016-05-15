from PyQt4 import QtSql, QtGui

def createDB():
   db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
   db.setDatabaseName('music.db')
	
   if not db.open():
      QtGui.QMessageBox.critical(None, QtGui.qApp.tr("Cannot open database"),
         QtGui.qApp.tr("Unable to establish a database connection.\n"
            "This example needs SQLite support. Please read "
            "the Qt SQL driver documentation for information "
            "how to build it.\n\n" "Click Cancel to exit."),
         QtGui.QMessageBox.Cancel)
			
      return False
		
   query = QtSql.QSqlQuery()
	
   query.exec_("create table people(id int primary key, vk_id varchar(30),"
      "firstname varchar(20), lastname varchar(20))")
   
   query.exec_("create table songs(id int primary key, performer varchar(50),"
      "songname varchar(100))")

   query.exec_("create table user_songs(id_user int, id_song int,"
       "FOREIGN KEY(id_user) REFERENCES people(id),"
       "FOREIGN KEY(id_song) REFERENCES songs(id))")
		
   return True
