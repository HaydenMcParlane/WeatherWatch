import urllib2
import customhttp
import customexception

class CustomUrlLib2(customhttp.CustomHttp):
    MODULE_NAME = 'customurllib2'
    CLASS_NAME = 'CustomUrlLib2'
        
    FUNC_GET = 'get()'
    @staticmethod    
    def get(url):
        try:
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            payload = response.read()
            response.close()
            return payload
        except Exception as e:
            customexception.CustomException.getExceptionMsg(e, "customurllib2", 'CustomUrlLib2', 'get()')
    
    FUNC_GET_AUTH = 'getAuth()'
    @staticmethod    
    def getAuth(url ,username, password):
        try:
            req = urllib2.Request(url,headers={'Content-Type':'application/json'})            
            password_mngr = urllib2.HTTPPasswordMgrWithDefaultRealm()            
            password_mngr.add_password(None, url, username, password)            
            auth_handler = urllib2.HTTPBasicAuthHandler(password_mngr)
            opener = urllib2.build_opener(auth_handler)
            urllib2.install_opener(opener)
            response = urllib2.urlopen(req)
            payload = response.read()
            print payload   
            response.close()         
            return payload
        except Exception as e:
            customexception.CustomException.getExceptionMsg(e, "customurllib2", 'CustomUrlLib2', 'getAuth()')
    
    def put(self, url, headers, data):
        raise NotImplementedError("\nPlease implement put() method : CustomHttp Subclass\n")
    
    def post(self, url, headers, data):
        raise NotImplementedError("\nPlease implement post() method : CustomHttp Subclass\n")
    
    FUNC_POST_AUTH = 'postAuth()'
    @staticmethod
    def postAuth(url, str_jsonData, username, password):
        try:                        
            req = urllib2.Request(url, data=str_jsonData, headers={'Content-Type':'application/json'})            
            password_mngr = urllib2.HTTPPasswordMgrWithDefaultRealm()            
            password_mngr.add_password(None, url, username, password)            
            auth_handler = urllib2.HTTPBasicAuthHandler(password_mngr)
            opener = urllib2.build_opener(auth_handler)
            urllib2.install_opener(opener)
            response = urllib2.urlopen(req)
            payload = response.read()
            print payload   
            response.close()         
            return payload
        except Exception as e:
            customexception.CustomException.getExceptionMsg(e, "customurllib2", 'CustomUrlLib2', 'postAuth()')
    
    def delete(self, url, headers):
        raise NotImplementedError("\nPlease implement delete() method : CustomHttp Subclass\n")