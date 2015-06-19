from lxml import html
from colorama import init
init() #init() Needed for colorama
from colorama import Fore
import requests
import sys

#D: Function to get temperature using weather underground
#I: String city and String state.
#O: Floating point number representing the temperature in that area.
def getTemperature(city, state):
    try:        
        url = "http://www.wunderground.com/cgi-bin/findweather/getForecast?query=" + city + "%2C+" + state + "&MR=1"
        response = requests.get(url)
        htmlTree = html.fromstring(response.text)
        currentTemp = (htmlTree.xpath('//*[@id="curTemp"]/span/span[1]/text()'))[0]
        return currentTemp
    except:
        #Exception handle
        return                  
    
def getTemperatureColor(temperature):
    if temperature < 40.0:
        color = Fore.BLUE
    elif temperature <= 65.0:
        color = Fore.CYAN
    elif temperature <= 90.0:
        color = Fore.YELLOW
    else:
        color = Fore.RED    
    return color

def main():    
    try:    
        curCity = sys.argv[1]
        curState = sys.argv[2]
        temperature = getTemperature(curCity, curState)
        color = getTemperatureColor(float(temperature))            
        print(color + temperature)
    except:
        print "\nYou need to enter the City and State. Please try again.\n"    


if __name__ == "__main__":
    main()