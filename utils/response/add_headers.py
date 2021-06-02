from flask import Response
from functools import wraps


def add_header(headers: dict) -> Response:
	def inner_function(incoming_request):
		@wraps(incoming_request)
		def wrapper():
			response = incoming_request()
			response.headers |= headers # for some reason this shows an error in pycharm but it works ok
			return response
		
		return wrapper
	
	return inner_function
