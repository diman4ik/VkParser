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
			
      return None
		
   query = QtSql.QSqlQuery()
	
   query.exec_("create table people(id int primary key, vk_id varchar(30), city varchar(60), sex int, age int,"
      "firstname varchar(25), lastname varchar(25))")
   
   query.exec_("create table songs(id int primary key, performer varchar(50),"
      "songname varchar(100))")

   query.exec_("create table user_songs(id_user int, id_song int,"
       "FOREIGN KEY(id_user) REFERENCES people(id),"
       "FOREIGN KEY(id_song) REFERENCES songs(id))")
		
   return db
   
count = 0
   
def addUser(vk_id, first_name, last_name, sex, city, age):
    query = QtSql.QSqlQuery()
    
    global count
    print("insert " + str(count))
    count += 1
    
    query.prepare("INSERT INTO people (id, vk_id, city, sex, age, firstname, lastname)"
                   " VALUES (?, ?, ?, ?, ?, ?, ?)")
    
    query.addBindValue(int(vk_id))
    query.addBindValue("id" + str(vk_id))
    query.addBindValue(city)
    query.addBindValue(sex)
    query.addBindValue(age)
    query.addBindValue(first_name)
    query.addBindValue(last_name)

    query.exec_()
    
def getUsersCount():
    query = QtSql.QSqlQuery()
    
    query.prepare("select count(*) from people")
    query.exec_()
    query.first()
    return query.value(0)

def selectUsers():
    model = QtSql.QSqlQueryModel()
    model.setQuery("SELECT vk_id || ' ' || firstname || ' ' || lastname FROM people order by id")
    #model.setQuery("SELECT * FROM people order by id")
    return model
