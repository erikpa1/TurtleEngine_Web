import sqlite3 as sql
import os




class DatabaseManager:

    def __init__(self, databaseFolder: str = 'database'):
        self.database = sql.connect(os.path.abspath('./' + databaseFolder + '.db'))
        self._init_users()

    def _init_users(self):
        self.database.execute("create table if not exists users (name text, email text, password text, registration_date integer)")

    def _init_assets(self): pass

    def SerializeClass(self, object):
        serializator = type(object).DATABASE_SERIALIZATOR(object)
        insert = serializator.GetInsert()
        print("Inserting: " + insert)
        self.database.execute(insert)

    #Database overridings
    def execute(self, order):
        self.database.execute(order)
    #========


    def GetAllUsers(self):
        return self.database.execute("SELECT * from users")


db = None