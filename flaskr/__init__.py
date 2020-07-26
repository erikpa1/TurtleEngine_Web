import os

from flask import Flask
from flask import render_template

def CreateApp(test_config = None):

    app = Flask("TurtleEngine", instance_relative_config = True, template_folder="")
    app.config.from_mapping(
        SECRET_KEY = 'dev'
    )
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def hello():
        return render_template('index.html')

    print("Flask app created")
    return app

app = CreateApp()
app.run(debug = True)





