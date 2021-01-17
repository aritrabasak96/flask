from flask import Flask, request, render_template,url_for

app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0



@app.route("/")
def homepage():
    # get popular cakes images
    # get recommended cakes images
    # get other cakes images
    return render_template("index.html",name="aritra")



if __name__ == "__main__":
    app.run(debug=True,port=2400)
