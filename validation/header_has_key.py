from flask import request
from functools import wraps
import json
from NotFound import NotFound


def header_has_key(header_name: str, key: str):
    """ The decorator checks if the parsed json has a certain value in it
        Assumes the header is there and can be parsed as json
    """

    def inner_function(incoming_request):

        @wraps(incoming_request)
        def wrapper():
            header = request.headers[header_name]
            parsed_header = json.loads(header)
            if key not in parsed_header.keys():
                return json.dumps({"response": f"Header '{header_name}' did not include required key '{key}'"}), 400
            return incoming_request()

        return wrapper

    return inner_function
