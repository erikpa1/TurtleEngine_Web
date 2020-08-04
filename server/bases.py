from flask import render_template


class DatabaseSerializator:
    def GetSelect(self):
        return ""

    def GetInsert(self):
        return ""

    def GetUpdate(self):
        return ""



class Screen():
    def RenderTemplate(self, template, **context):
        return render_template(template, **context)

