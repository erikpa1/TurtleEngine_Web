from server.bases import Screen

class ScreenLogin(Screen):

    def RenderTemplate(self):
        return super().RenderTemplate("server/screen_login.html")

