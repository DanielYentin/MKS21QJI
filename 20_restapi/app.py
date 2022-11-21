# TNPG: Daniel Yentin, <Frist> <Lsat>
# SoftDev
# K<nn> -- <Title/Topic/Summary... (Aim for concision, brevity, CLARITY. Write to your future self...)>
# 2022-11-23
# time spent: .5 

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