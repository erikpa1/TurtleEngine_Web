from server import app
from server import rm

from server.database_user_manager import UsersManager

from server.screen_login import ScreenLogin
from server.screen_main import ScreenMain


loginScreen = ScreenLogin()
loginManager = UsersManager()
mainScreen = ScreenMain()

@app.route('/')
@app.route('/login')
def main():
    #return loginScreen.GetDefaultScreen()
    return mainScreen.GetDefaultScreen()

@app.route('/login_submit', methods=['GET', 'POST'])
def tryLogin():
    loginStatus = loginManager.LoginCheck(rm.GetForm()["uname"], rm.GetForm()["pswd"])
    return mainScreen.GetDefaultScreen() if loginStatus else loginScreen.GetLoginFailedScreen()




app.run(debug = True)
