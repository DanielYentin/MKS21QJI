# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2022

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    return "No hablo queso!"

app.run()

'''
We learned that the print name in the hello_world function is non-essential to running the actual html page. 
We also learned that the run function somehow runs the

'''
