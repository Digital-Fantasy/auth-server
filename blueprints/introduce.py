# coding=utf-8
import json

import jwt
from flask import Blueprint, request, make_response


from utils import response
import validation
from graphql_client import gql
from validation.validate import validate_name, validate_bio, validate_picture, validate_nickname, validate_phone_number, validate_username
from validation.Exceptions import BioTooLong
introduce_blueprint = Blueprint('introduce', __name__)


@introduce_blueprint.route("/introduce", methods=["GET"])
@response.set_content_header("application/json; charset=utf-8")
def introduce_get():
    """
    Get request handler
    """
    body = {"response": "Introductions should be a post request"}
    status = 405
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    r = make_response(body, status)
    r.headers["Content-Type"] = "application/json; charset=utf-8"
    return r


@introduce_blueprint.route("/introduce", methods=["POST"])
@validation.body_is_json()
@validation.body_has_key("username")
@validation.body_has_key("pwd")
@validation.body_key_content_min_length("pwd", 6)
@response.set_content_header("application/json; charset=utf-8")
def introduce_post():
    """
    Post request handler
    """
    introduction = request.get_json(force=True)
    username = introduction["username"]
    phone_number = introduction.get("phone_number", None)
    nickname = introduction.get("nickname", None)
    bio = introduction.get("bio", "No bio yet")
    name = introduction.get("name", None)
    picture = introduction.get("picture", None)

    try:
        bio = validate_bio(bio, 500)
    except BioTooLong as tooLong:
        return make_response({"response": tooLong.message}, 400)

    try:
        phone_number = validate_phone_number(phone_number)
        picture = validate_picture(picture)
        name = validate_name(name, username)
        nickname = validate_nickname(nickname, username)
        username = validate_username(username, username)
    except Exception as error:
        raise error

    # Add more handeling here!

    variables = {"bio": bio,
             "name": name,
             "nickname": nickname,
             "phone_number": phone_number,
             "username": username,
             "pwd": introduction["pwd"],
             "picture":picture}
    query = """
            mutation AddUser($bio: String = "", $name: String! = "", $picture: String = "", $phone_number: String = "", $nickname: String = "", $username: String!, $pwd:String!) {
              addUser(input: {username: $username, bio: $bio, name: $name, nickname: $nickname, phone_number: $phone_number, picture: $picture, pwd:$pwd}) {
                user {
                  id
                }
              }
            }
        """
    print(variables)
    response = gql.execute(query, variables)
    # look at response and send response back
    print(response)
    encoded_jwt = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")
    body = {"response": ":_-_: Welcome :_-_:", "jwt": encoded_jwt, "dgraph_response": response}
    status = 200
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    r = make_response(body, status, headers)
    r.headers["Content-Type"] = "application/json; charset=utf-8"
    return r

# https://github.com/Alesh/jwt4auth/blob/master/sample/backend.py


'''
@auth(
    add: { rule: """
        query Getuser($NAME: String, $NICKNAME: String, $PICTURE: String, $USER: String!) {
  queryUser(filter: {username: {eq: $USER}, picture: {eq: $PICTURE}, nickname: {eq: $NICKNAME}, name: {eq: $NAME}}) {
    username
  }
}
"""
  }
)
'''
