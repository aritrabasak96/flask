from flask import Blueprint

from .extensions import mongo

main = Blueprint('main',__name__)  # create a Blueprint

# CRUD operation


@main.route("/")
def index():
    user = mongo.db.users # create a user collections
    user.insert({'name':'aritra'})
    return 'done'


# find
@main.route("/find")
def find():
    user = mongo.db.users
    print('user',user)
    data =  user.find_one({'name':'aritra'})
    print(data['name'])
    return 'find'

# update
@main.route("/update")
def update():
    user = mongo.db.users
    data = user.find_one({'name':'aritra'})

    data['name'] = 'coder'
    user.save(data)
    return 'updated'

# delete
