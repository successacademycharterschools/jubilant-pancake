# External
from flask import jsonify

class InvalidUsage(Exception):
    """Returns error code and message"""
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        output = dict(self.payload or ())
        output['message'] = self.message
        return output
