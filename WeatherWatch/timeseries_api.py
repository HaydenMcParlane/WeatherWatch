import os
import json
import restapi
import customhttp
import exceptions
import customurllib2

class TimeSeriesApi:
    MODULE_NAME = 'timeseries_api'
    CLASS_NAME = 'TimeSeriesApi'    
    USERNAME = ''
    PASSWORD = ''    
    BASE_URL = ''        
    
    def __init__(self):
        JCRED = json.loads(os.environ.get("VCAP_SERVICES"))['timeseriesdatabase'][0]['credentials']
        USERNAME = JCRED['username']
        PASSWORD = JCRED['password']
        HOST = JCRED['host']
        PORT = str(JCRED['rest_port'])
        DB = JCRED['db']
#         BASE_URL = JCRED['rest_url']
        self.USERNAME = JCRED['username']
        self.PASSWORD = JCRED['password']
        self.BASE_URL = 'https://' + HOST + ":" + PORT + "/" + DB                
    
    FUNC_GET = 'get()'
    def find(self, dict_constraint=None):
        if dict_constraint == None:    
            url = self.BASE_URL + "/data?"           
            jsonPayload = json.loads(customurllib2.CustomUrlLib2.getAuth(url, self.USERNAME, self.PASSWORD))            
            return jsonPayload
        else:
            raise NotImplementedError("else portion of if-else in Mod [" + self.MODULE_NAME + "] ---> Class [" + self.FUNC_GET + "]"
                                      + " ---> Func [" + self.FUNC_GET + "] hasn't yet been implemented. Implement before using.")
        
    FUNC_INSERT = 'insert()'
    def insert(self, str_jsonData):
        try:    
            url = self.BASE_URL + "/data"
            jsonPayload = customurllib2.CustomUrlLib2.postAuth(url, str_jsonData, self.USERNAME, self.PASSWORD)            
            return jsonPayload
        except Exception as e:
            raise NotImplementedError("else portion of if-else in Mod [" + self.MODULE_NAME + "] ---> Class [" + self.CLASS_NAME + "]"
                                      + " ---> Func [" + self.FUNC_INSERT + "] hasn't yet been implemented. Implement before using.")
            
#     def createCollection(self, collectionName):
#         try:
#             url = self.BASE_URL
#             print '\n******In TimeSeries createCollection() : url = ' + url + "******\n"#DEBUG
#             jsonPayload = customurllib2.CustomUrlLib2.postAuth(url)
#         except Exception as e: