from flask import request, make_response
from functools import wraps


def body_is_json():
    """Looks if the body of the request can be turned into a dict"""
    def inner_function(incoming_request):

        @wraps(incoming_request)
        def wrapper():
            try:
                request.get_json(force=True)
            except Exception as error:
                return make_response({"response":"Could not parse json in request", "exception":error.__str__()}, 400)
            return incoming_request()
        return wrapper
    return inner_function