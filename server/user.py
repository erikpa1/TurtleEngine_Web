from server.bases import DatabaseSerializator
from datetime import datetime

class UserDatabaseSerializator(DatabaseSerializator):

    def __init__(self, user):
        self.user = user

    def GetInsert(self):
        #TODO1 look how can i look on this easier
        name = self.user.name
        email = self.user.email
        password = self.user.password
        creation = datetime.now().microsecond
        insert = "insert into users values" + str((name, email, password, creation))
        return insert



class User:

    DATABASE_SERIALIZATOR = UserDatabaseSerializator

    def __init__(self):
        self.name = ""
        self.email = ""
        self.password = ""
        self.creationTime = -1

    def SetName(self, value: str):
        self.name = value

    def SetEmail(self, value: str):
        self.email = value

    def SetPassword(self, value: str):
        #TODO2 password encryption here
        self.password = value
