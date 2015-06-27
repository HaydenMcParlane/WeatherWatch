from lxml import html
import urllib2
import requests
import sys

MODULE_NAME = 'gweather'
CLASS_NAME = 'N/A'

#D: Function to get temperature using weather underground
#I: String city and String state.
#O: Floating point number representing the temperature in that area.
FUNC_GET_TEMPERATURE = 'getTemperature()'
def getTemperature(city, state):
    try:                        
        url = "http://www.wunderground.com/cgi-bin/findweather/getForecast?query=" + city + "%2C+" + state + "&MR=1"        
        response = urllib2.urlopen(url)        
        text = response.read()        
        htmlTree = html.fromstring(text)
        currentTemp = (htmlTree.xpath('//*[@id="curTemp"]/span/span[1]/text()'))[0]
        return currentTemp
    except Exception as e:
        return customexception.CustomException(e, self.MODULE_NAME, self.CLASS_NAME, self.FUNC_GET_TEMPERATURE)  
