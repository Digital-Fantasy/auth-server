from flask import request
from functools import wraps
import json

def has_header(header_name: str):
    """ A decorator that checks if the request has a certain header if it doesn't it will automatically return a response saying the header is missing """

    def inner_function(incoming_request):

        @wraps(incoming_request)
        def wrapper():
            headers = request.headers.keys()
            if header_name not in headers:
                return json.dumps({"response": f"'{header_name}\' header not present in request"}), 400
            else:
                return incoming_request()

        return wrapper

    return inner_function
