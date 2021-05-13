from flask import request
from functools import wraps
import json
from NotFound import NotFound


def header_is_json(header_name: str):
    """The decorator checks if the header can be parsed as json"""

    def inner_function(incoming_request):

        @wraps(incoming_request)
        def wrapper():
            header = request.headers.get(header_name, NotFound)
            try:
                json.loads(header)
            except Exception as e:
                return json.dumps({"response": f"Could not parse header: '{header_name}\'. While trying an exeption was raised. Check if you are sending valid json",
                                   "exception": e.__str__()}), 400
            return incoming_request()

        return wrapper

    return inner_function
