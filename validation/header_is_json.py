from flask import request
from functools import wraps
import json


def header_is_json(header_name: str):
    """The decorator checks if the header can be parsed as json"""

    def inner_function(incoming_request):

        @wraps(incoming_request)
        def wrapper():
            try:
                header = request.headers.get(header_name)
                json.loads(header)
            except Exception as e:
                return {"response": f"Could not parse header: {header_name}. While trying an exeption was raised. Check if you are sending valid json",
                                   "exception": f"{e.__str__()}"}, 400
            return incoming_request()

        return wrapper

    return inner_function
