from server.bases import Screen

class ScreenLogin(Screen):

    def GetDefaultScreen(self):
        return super().RenderTemplate("server/screen_login.html", password_validity="")

    def GetLoginFailedScreen(self):
        return super().RenderTemplate("server/screen_login.html", password_validity="Invalid password")


