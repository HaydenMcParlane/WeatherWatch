'''
Created on Jun 17, 2015

@author: Hayden
'''
import os
import json
import datetime
import restapi
import timeseries_api
import customexception
from gweather import getTemperature
import requests
from requests.auth import HTTPBasicAuth
from flask import render_template
from flask import jsonify
from flask import make_response
from flask import Flask
app = Flask(__name__)

# On Bluemix, get the port number from the environment variable VCAP_APP_PORT
# When running this app on the local machine, default the port to 8080
port = int(os.getenv('VCAP_APP_PORT', 8000))

#Module Consts
MODULE_NAME = 'server'
CLASS_NAME = 'N/A'

FUNC_GET_DATA = 'getData()'
@app.route('/get-data')
def getData():        
    try:       
        tsApi = timeseries_api.TimeSeriesApi()
        jResult = tsApi.find()
        return json.dumps(jResult)
    except Exception as e:
        return customexception.CustomException.getExceptionMsg(e, MODULE_NAME, CLASS_NAME, FUNC_GET_DATA)
    
@app.route("/api/temperature/<city>/<state>")
def getTemp(city, state):
    temp = getTemperature(city, state)
    date_time = datetime.datetime.now()            
    timeseries_data = ('{ city:"%s", state:"%s", temperature:%s, date-time:"%s" }' % (city, state, temp, date_time))    
    tsApi = timeseries_api.TimeSeriesApi()
    jsonResult = tsApi.insert(timeseries_data)
    response = make_response(jsonify({"temperature": temp}))
    response.headers['Access-Control-Allow-Origin'] = "*"
    response.headers['Content-Type'] = "application/json"    
    return response

@app.route("/", methods=["GET", "POST"])
def home():       
    return render_template('home.html')

@app.route("/ViewData", methods=["GET", "POST"])
def viewData():       
    return render_template('viewdata.html')

@app.route("/hello")
def hello():
    return "Hello!"

@app.route("/hello/<name>")
def helloName(name=None):
    return "Hello " + name

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)    