from flask import Flask, request , jsonify, make_response
import jwt
import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"


# middleware to check the user is http Authenticate or not
def decorate_route(f):
    def decorate(*args,**kargs):
        auth = request.authorization
        print(auth)
        if auth and auth.username == 'aritra8' and auth.password == 'password':
            return f(*args,**kargs)
        return make_response('could not verified',401,{'www-Authenticate': 'Basic realm="Login Required"'})
    return decorate

# middleware to check if the user has a valid token or not
def valid_token(f):
    def decorates(*args,**kargs):
        token = request.args.get('token')  # args get data like that localhost:5000/view?token=kdnfknsfkkb
        try:
            decode_data = jwt.decode(token,app.config['SECRET_KEY'])
            print('decode_data------------------',decode_data)
        except:
            return "token is invalid"
        else:
            return f(*args,**kargs)

    return decorates

# login route return an jwt token

@app.route("/login")
@decorate_route
def login():
    # create jwt token
    auth = request.authorization
    # jwt.encode({'user':'','exp':'expiration time of the token','secret key'})
    token =  jwt.encode({'user':auth.username,'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=2)},app.config['SECRET_KEY'])
    print(token.decode('UTF-8'))
    return "<p>{}</p>".format(token.decode('UTF-8'))


# now create a route
@app.route("/view")
@valid_token
def view():
   return "enjoy"



if __name__ == "__main__":
    app.run(debug=True,port=4060)
