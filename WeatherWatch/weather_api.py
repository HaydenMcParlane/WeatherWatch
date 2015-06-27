import restapi
import customhttp
import customrequests
import json

class WeatherApi(restapi.RestApi):
    BASE_URL = "http://www.wunderground.com/cgi-bin/findweather/getForecast?query="
    MID_URL1 = "%2C+"
    END_URL = "&MR=1"
    CITY = 'city'
    STATE = 'state'
    url = ''
    def get(self, dict_constraint):
        url = self.BASE_URL + dict_constraint[self.CITY] + self.MID_URL1 + dict_constraint[self.STATE] + self.END_URL
        print 'In WUnderground get() : url = ' + url #DEBUG
        response = customrequests.get(url)
        return json.loads(response.text)
        