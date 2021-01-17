from flask import Flask, request
from flask_pymongo import PyMongo
import random


app = Flask(__name__)

app.config['MONGO_URI'] = "mongodb://localhost:27017/myFriendname"

mongo = PyMongo(app)



@app.route("/")
def addData():
    data = mongo.db.users
    first_name = ('aritra','debesh','souvik','bama','abhishek','dibu')
    last_name = ('basak','sil','ghosh','saha','chakraborty','biswas','sen','laha','brue','samrat')
    address = ('shyambazar','shobhabazar','goria','howrah','hoogly','tala','sithi')
    age = (21,22,23,25,24,28,19,20)


    for i in range(0,100000):

        name = random.choice(first_name) + " " + random.choice(last_name)
        add = random.choice(address)
        ag = random.choice(age)
        data.insert({'id':i,'name':name,'address':add,'age':ag})

    return 'done'

@app.route('/find/<id>')
def findData(id):

    data = mongo.db.users
    findData =  data.find_one_or_404({'id':id})
    return '<h1>name{}, address {}, age {}<h1>'.format(finddata['name'],finddata['address'],findData['age'])


if __name__ == "__main__":

    app.run(debug=True)
