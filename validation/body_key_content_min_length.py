from flask import request
from functools import wraps


def body_key_content_min_length(key: str, min_length: int):
    """ Checks if a value of a key in the body has a certian length
        Assumes the body is there and can be parsed as json
    """
    def inner_function(incoming_request):

        @wraps(incoming_request)
        def wrapper():
            # try:
            body = request.get_json(force=True)
            if key not in body.keys():
                return {"response": f"Body did not have required key {key}"}, 400
            if len(body[key]) < min_length:
                return {"response": f"Value of {key} field in body is not long enough. Minimum length is {min_length}."}, 400
            return incoming_request()

        # except Exception as error:
        #     return {"response": f"Could not parse json in body", "exception": str(error)}, 400

        return wrapper

    return inner_function
