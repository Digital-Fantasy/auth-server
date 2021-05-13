from flask import Blueprint, render_template, request, redirect, flash
import jwt
import validation

get_token_blueprint = Blueprint('get_token', __name__)


@get_token_blueprint.route("/get_token", methods=["POST"])
@validation.has_header("data")
@validation.header_is_json("data")
@validation.header_has_key("data", "username")
@validation.header_has_key("data", "password")
def get_token_post():
    return "NIY"


# https://docs.aiohttp.org/en/stable/ https://pypi.org/project/jwt4auth/ https://pypi.org/project/jwt4auth/https://pypi.org/project/jwt4auth/https://pypi.org/project/jwt4auth/