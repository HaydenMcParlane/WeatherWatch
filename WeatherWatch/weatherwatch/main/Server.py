'''
Created on Jun 17, 2015

@author: Hayden
'''
from gweather import getTemperature
from flask import render_template
from flask import jsonify
from flask import make_response
from flask import Flask
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello!"

@app.route("/hello/<name>")
def helloName(name=None):
    return "Hello " + name

@app.route("/api/temperature/<city>/<state>")
def getTemp(city, state):
    temp = getTemperature(city, state)
    response = make_response(jsonify({"temperature": temp}))
    response.headers['Access-Control-Allow-Origin'] = "*"
    response.headers['Content-Type'] = "application/json"
    return response

@app.route("/", methods=["GET", "POST"])
def index():       
    return render_template('weatherwatch.html')

if __name__ == "__main__":
    app.run()