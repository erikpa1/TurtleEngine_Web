from server.bases import Screen

from meta.codebuilders.html_constants import *
from meta.codebuilders.html import *
from meta.codebuilders.html_bootstrap import *


class ScreenMain(Screen):


    def GetMetaLogin(self):
        tmp = HtmlDocument()

        tmp.head.AddBootstrapRequirment()

        bar: bsNavBar = tmp.body.AddNode(bsNavBar())

        bar.AddNavItem(bsNavItem("About"))
        bar.AddNavItem(bsNavItem("About"))
        bar.AddNavItem(bsNavItem("Store"))
        bar.AddNavItem(bsNavItem("Cloud"))
        bar.AddNavItem(bsNavDropDownItem("Editors", ["Spot", "Map", "Tour"]))

        tmp.body.AddNode(bsBreak())

        container: bsContainer = tmp.body.AddNode(bsContainer())
        container.AddItem(bsHeader3("Navbar with dropdown"))
        container.AddItem(bsParagraph("This is example of the generated dropdown"))

        return tmp.ToString()



    def GetDefaultScreen(self):
        #return super().RenderTemplate("server/screen_main.html")
        tmp = self.GetMetaLogin()
        print(tmp)
        return tmp