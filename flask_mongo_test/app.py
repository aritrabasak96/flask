from flask import Flask
from flask_pymongo import PyMongo

# configure flask app
app = Flask(__name__)

# configure mongodb database
app.config['MONGO_URI'] = "mongodb://localhost:27017/testpymongo"

mongo = PyMongo(app)

# create a document
@app.route("/")
def createDocument():
    data =  mongo.db.classroom
    data.insert({'name':'physicsclass','student':'30','average_age':'12'})
    data.insert({'name':'chemistry','student':'50','average_age':'17'})
    data.insert({'name':'mathclass','student':'150','average_age':'27'})
    data.insert({'name':'programming','student':'10','average_age':'22'})
    return 'create successfully'

# find
@app.route("/find")
def findDocument():
    data = mongo.db.classroom
    finddata = data.find_one_or_404({'name':'mathclass'})
    return '<h1>the tuition name is{}, total student is {}<h1>'.format(finddata['name'],finddata['student'])

# delete
@app.route("/delete/<username>")
def deleteDocument(username):
    data = mongo.db.classroom
    data.delete_one({'name':username})
    return 'success'

# update
@app.route("/update/<name>")
def updateDocument(name):
    data = mongo.db.classroom
    data.update_one({'name':name},{'$set':{'student':80}})
    return 'success'



if __name__ == "__main__":
    app.run(debug=True,port=8000)
