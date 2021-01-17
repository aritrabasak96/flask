from flask import Flask, request, jsonify, make_response, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# bacis http request

@app.route("/basic")
def basic():
    return "basic"

# basic json data
@app.route("/json")
def json():
    obj = {'name':'aritra','age':23,'skill':'development','roll':34,'education':['school','collge','university']}
    return jsonify({'body':obj})

# custom http request
@app.route("/custom")
def custom():
    my_custom = make_response('nice')
    my_custom.status_code = 101
    my_custom.set_cookie('setcookie','75836485mfbdmnfdfvvh')
    my_custom.set_cookie('setcookie2','12fgterer555353553')
    return my_custom

@app.route("/getcookie")
def getcookie():
    # request.cookies.get('setcookie')
    pass



# .................. session storage ..........
@app.route('/session')
def sessionData():
   session['response'] = 'session data'  # this will add a session in the session dict
   s = session.pop('response',None) # this will pop the session from the session dict
   print('session---------------',s)
   return 'done'

@app.route('/getsession')
def getsession():
    s = session['response']
    return '<p>session is {}</p>'.format(s)

if __name__ == "__main__":
    app.run(debug=True,port=5000)
