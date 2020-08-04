from server.database import db

class UsersManager:

    LOGIN_FAIL_WRONG_PASSWORD = 0
    LOGIN_FAIL_NONEXISTING_USER = 1
    LOGIN_SUCCESS = 1

    def LoginCheck(self, username: str, password: str):
        pass

    def GetUser(self, username: str, password: str):
        pass



