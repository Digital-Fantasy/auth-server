from flask import Blueprint, render_template, request, redirect, flash
import validation
import json
from graphql_client import gql
import jwt

introduce_blueprint = Blueprint('introduce', __name__)


@introduce_blueprint.route("/introduce", methods=["GET"])
def introduce_get():
    print(request.headers)
    # Get header from request
    print(type(request.headers))

    return json.dumps(
        {"response": "Introductions should be a post request. Also don't forget to include a data json header. Data should have a username, email and password!"}), 405


@introduce_blueprint.route("/introduce", methods=["POST"])
@validation.has_header("data")
@validation.header_is_json("data")
@validation.header_has_key("data", "username")
@validation.header_has_key("data", "email")
@validation.header_has_key("data", "password")
def introduce_post():
    introduction = request.headers.get("data")
    variables = {"username": introduction["username"], "email": introduction["email"], "password": introduction["password"]}
    query = """
        mutation addUSer(vars bal bal) {
            human {
                id
                username
                email
            }   
        
        }
    """
    response = gql.execute(query, variables)
    # look at response and send response back
    encoded_jwt = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")
    return json.dumps({"response": "Did you introduce yourself?", "jwt": encoded_jwt})
# https://github.com/Alesh/jwt4auth/blob/master/sample/backend.py
