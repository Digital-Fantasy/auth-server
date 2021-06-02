from flask import Response
from functools import wraps


def set_content_header(content_type: str) -> Response:
	def inner_function(incoming_request):
		
		@wraps(incoming_request)
		def wrapper():
			response = incoming_request()
			response.headers["Content-Type"] = content_type
			return response
		
		return wrapper
	
	return inner_function
