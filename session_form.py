from flask import Flask, render_template,request, url_for
from flask_session import Session
from flask_bootstrap import Bootstrap
from registrationForm import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissecret!'
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
# Session(app)
Bootstrap(app)

creds_dict={loginForm.username : "admin", loginForm.password :"admin"}
@app.route('/', methods=["GET","POST"])
def login():

    form = loginForm()
    print("hi")
    if request.method == 'GET':
        print("request recieved")
        return render_template("login.html", form=form)
    else:
        return " Welcome to a new page  "

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True, port=5000)





