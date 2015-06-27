import exceptions

class RestApi:
    def get(self, dict_constraint):
        raise NotImplementedError('\nPlease Implement get() method : RestApi Subclass\n')
    
    def put(self, dict_data):
        raise NotImplementedError('\nPlease Implement put() method : RestApi Subclass\n')
    
    def post(self, dict_data):
        raise NotImplementedError('\nPlease Implement post() method : RestApi Subclass\n')
    
    def delete(self, dict_constraint):
        raise NotImplementedError('\nPlease Implement delete() method : RestApi Subclass\n')
    