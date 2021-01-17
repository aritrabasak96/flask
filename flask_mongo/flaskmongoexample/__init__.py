# __init__ function will execute as soon as an object of a class initialize
# all the initialization

from flask import Flask

from .extensions import mongo

from .main import main

def create_app(config_object = 'flaskmongoexample.settings'):

    app = Flask(__name__)
    app.config.from_object(config_object) # configure the app here
    app.register_blueprint(main)

    mongo.init_app(app)

    return app
