import customhttp
import customexception
import requests

class CustomRequests(customhttp.CustomHttp):
    MODULE_NAME = 'customrequests'
    CLASS_NAME = 'CustomRequests'
    def get(self, url):
        try:
            response = requests.get(url)
            payload = response.text            
            response.headers['Content-Type'] = "application/json"
            raise NotImplementedError('\n***** The CustomRequests module hasn\'t been fully implemented. Please implement' +
                                      'before using. *****\n')
            return payload
        except Exception as e:
            print customexception.getExceptionMsg(e, self.MODULE_NAME, self.CLASS_NAME)