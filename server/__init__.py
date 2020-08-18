from flask import Flask, request
from flask_bootstrap import Bootstrap


class RuntimeManager:

    @staticmethod
    def GetMethod():
        return request.method

    @staticmethod
    def GetForm():
        return request.form

    @staticmethod
    def IsPost():
        return request.method == "POST"

    @staticmethod
    def IsGet():
        return  request.method == "GET"

rm = RuntimeManager





app = Flask("TurtleEngine", instance_relative_config = True, template_folder="../")
#Bootstrap(app)
