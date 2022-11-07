# <div ID="success"></div>: Daniel Yentin, Ivan Yeung
# SoftDev
# Nov 2022

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
from flask import session           #facilitate form submission
from flask import redirect           #facilitate form submission
from flask import url_for

username = "test"
password = "1234"

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object
app.secret_key = b"\xdcG4g\xebL\x98m\xacX\x03\x13\xef\xfeF0#\x07P\x07JN\xf1P|'\x9ak\x1f\xe2\xf2?"

@app.route("/", methods=['GET', 'POST'])
def root():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    #checks if cookie has username and password stored
    if ('username' in session):
        print("***DIAG: user has already logged  ***")
        return redirect(url_for("response"), 307)
    else:
        #returns login page if cookie does not have that information
        return redirect(url_for("login"), 307)

@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template('login.html')
    
@app.route("/auth", methods=['GET', 'POST'])
def login_auth():
    print("test")
    #checks if input for the username form matches with hardcoded username
    if (request.form["username"] == username):
        print("***DIAG: username matches ***")
        #checks if input for the password form matches with hardcoded password
        if (request.form["password"] == password):
            print("***DIAG: password matches ***")
            #when both coditions are met, password is stored in the cookie and the response page is rendered
            session["username"] = request.form["username"]
            return redirect(url_for("response"), 307)
        else:
            print("***DIAG: password did not match ***")
            return redirect(url_for("login"), 307)
    else:
        print("***DIAG: username did not match ***")
        return redirect(url_for("login"), 307)

@app.route("/logout", methods=['POST'])
# this function is called by the logout button when it is pressed on the response page
def logout():
    #cookie holding password is removed
    session.pop("username")
    print("***DIAG: password removed from cookie ***")
    return redirect(url_for("login"), 307)

@app.route("/response", methods=['POST'])
def response():
    return render_template('response.html')

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
