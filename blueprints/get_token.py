from flask import Blueprint, render_template, request, redirect, flash

get_token_blueprint = Blueprint('get_token', __name__)


@get_token_blueprint.route("/get_token", methods=["GET"])
def get_token_get():
    return render_template("get_token.html")


@get_token_blueprint.route("/get_token", methods=["POST"])
def get_token_post():
    return render_template("get_token.html")
