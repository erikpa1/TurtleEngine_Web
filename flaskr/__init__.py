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


    print("Flask app created")
    return app


@app.route('/')
def main():
    return "Hello"

app = CreateApp()
app.run(debug = True)