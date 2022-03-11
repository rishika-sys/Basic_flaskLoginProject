from flask import Flask, render_template,request, url_for
from flask_session import Session
from flask_bootstrap import Bootstrap
from registrationForm import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissecret!'
Bootstrap(app)

creds_dict={loginForm.username : "admin", loginForm.password :"admin"}
@app.route('/', methods=["GET","POST"])
def login():

    form = loginForm()
   
    if request.method == 'GET':
        return render_template("login.html", form=form)
    else:
        return " Welcome to a new page  "

if __name__ == '__main__':
    app.run(debug=True, port=5000)





