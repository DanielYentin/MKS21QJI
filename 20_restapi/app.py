# TNPG: Daniel Yentin, <Frist> <Lsat>
# SoftDev
# K<nn> -- <Title/Topic/Summary... (Aim for concision, brevity, CLARITY. Write to your future self...)>
# 2022-11-23
# time spent: .5 
# DISCO: 
#   1. the urllib library is used to make requests to a server, using the urlopen() function
#   2. the json library is used to parse the JSON data returned by the server

# QCC: 
#   1. what other libraries can be used instead of urllib?
#   2. what other serialization formats are there besides JSON and why is JSON prefered? 

import flask
from urllib.request import urlopen
import json

api = "https://api.nasa.gov/planetary/apod?api_key=0WqacuLbuMVfkaOdKQ2PExkzky1RZFFvlq59Gcxl"
app = flask.Flask(__name__)

@app.route("/")
def root():
    response = urlopen(api)
    data_json = json.loads(response.read())

    url = data_json["url"]
    explanation = data_json["explanation"]
    return flask.render_template("main.html", url=url, explanation=explanation)

if __name__ == "__main__":
    app.debug = True
    app.run()