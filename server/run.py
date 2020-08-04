from flask import Flask
from flask_bootstrap import Bootstrap

from server.screen_login import ScreenLogin


app = Flask("TurtleEngine", instance_relative_config = True, template_folder="../")
Bootstrap(app)

loginScreen = ScreenLogin()


@app.route('/')
@app.route('/login')
def main():
    return loginScreen.RenderTemplate()

@app.route('/login_submit', methods=['GET', 'POST'])
def tryLogin():
    return "Wrong"


app.run(debug = True)
