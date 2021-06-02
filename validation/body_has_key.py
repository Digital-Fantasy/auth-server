from flask import request
from functools import wraps
import json


def body_has_key(key: str, info=True):
    """ The decorator checks if the parsed json has a certain value in it
        Assumes the header is there and can be parsed as json.
        If info is false it wont give an informative reply
    """

    def inner_function(incoming_request):

        @wraps(incoming_request)
        def wrapper():
            # try:
                body = request.get_json(force=True)
                if key not in body.keys():
                    if info:
                        return {"response": f"Body did not have required key '{key}'"}, 400
                    else:
                        return {"response": f"Invalid request"}, 400
                return incoming_request()
            # except Exception as error:
            #     return {"response": f"Could not parse json in body", "exception": str(error)}, 400

        return wrapper

    return inner_function
