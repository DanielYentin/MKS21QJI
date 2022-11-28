# TNPG: Daniel Yentin, Kosta Dubovskiy
# SoftDev
# K20 -- Restfull APIs
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

api_key = ""
with open("key_nasa.txt", 'r') as f:
    api = "https://api.nasa.gov/planetary/apod?api_key="
    key = f.read().strip()
    api_key = api + key
    
app = flask.Flask(__name__)

@app.route("/")
def root():
    response = urlopen(api_key)
    data_json = json.loads(response.read())

    url = data_json["url"]
    explanation = data_json["explanation"]
    return flask.render_template("main.html", url=url, explanation=explanation)

if __name__ == "__main__":
    app.debug = True
    app.run()