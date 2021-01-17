from flask import Flask
from flask_restful import Resource,Api

app2 = Flask(__name__)
api = Api(app2)

from pro_app.views import views
