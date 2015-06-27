import exceptions

class CustomHttp:
    def get(self, url, headers):
        raise NotImplementedError("\nPlease implement get() method : CustomHttp Subclass\n")
    
    def put(self, url, headers, data):
        raise NotImplementedError("\nPlease implement put() method : CustomHttp Subclass\n")
    
    def post(self, url, headers, data):
        raise NotImplementedError("\nPlease implement post() method : CustomHttp Subclass\n")
    
    def delete(self, url, headers):
        raise NotImplementedError("\nPlease implement delete() method : CustomHttp Subclass\n")