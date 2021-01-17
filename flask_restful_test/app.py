from flask import Flask,request
from flask_restful import Resource,Api,marshal_with,fields
import json

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):

    def get(self):
        return {'msg':'hello welcome'},200

    def post(self):
        json_data = request.get_json()  # converted from json to dict
        # convert json into object
        return {'msg':json_data['msg']},200

class Parameter(Resource):

    def get(self,id):

        return {'msg':id}


# how to apply marshal_with

class UrgentItem(fields.Raw):
    def format(self, value):
        return "Urgent" if value & 0x01 else "Normal"

class UnreadItem(fields.Raw):
    def format(self, value):
        if value == "a":
            return 'valid'
        else:
            return 'not valid'

fields = {
    'name': fields.String,
    'priority': UrgentItem(attribute='flags'),
    'status': UnreadItem(attribute='flags'),
}



class  Userinfo(Resource):
       @marshal_with(fields)
       def get(self):
           return {'status':format("a")}



api.add_resource(HelloWorld,'/make')
api.add_resource(Userinfo,'/userinfo/')
api.add_resource(Parameter,'/get/<int:id>')

if __name__ == "__main__":
    app.run(debug=True,port=3000)
