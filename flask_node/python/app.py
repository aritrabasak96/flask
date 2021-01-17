from flask import Flask,request
from flask_restful import Api,Resource
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app, resources={r"/apinn/*": {"origins": "file:///H:/flask/flask_node/index.html"}})


class HelloNode(Resource):

    def get(self):
        return {'msg':'hello node how are you'}


api.add_resource(HelloNode,"/api/")

if __name__ == "__main__":
    app.run(port=5000)
