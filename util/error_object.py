from flask import jsonify

class ErrorObject:
    # TODO: implement ErrorObject
    # variables:
    #   - status_code(status code): int
    #   - error_message: str
    # functions:
    #   - __init__(self, status_code, message)
    #   - get_response(self): "{message}, status_code" format, same with Flask default response format
    def __init__(self, status_code, error_message):
        self.status_code = status_code
        self.error_message = error_message
        
    def get_response(self):
        return {"message": self.error_message}, self.status_code