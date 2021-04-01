import os
from server.database import DatabaseManager
from server.database import db

from server.user import User

databaseName = "database_test"

os.remove(os.path.abspath('./' + databaseName + ".db"))


db = DatabaseManager(databaseName)

user1 = User()
user1.SetName("Erik Palencik")
user1.SetEmail("erik.palencik@notexisting.com")
user1.SetPassword("1234567") #If you see this code i dont use this password anywhere, so dont even try

db.SerializeClass(user1)


rows = db.GetAllUsers().fetchall()

print("Writting all users:")
for row in rows:
    print(row)
