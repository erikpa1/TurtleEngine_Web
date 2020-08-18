from server.bases import Screen

class ScreenMain(Screen):

    def GetDefaultScreen(self):
        return super().RenderTemplate("server/screen_main.html")