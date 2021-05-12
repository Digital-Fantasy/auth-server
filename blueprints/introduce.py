from flask import Blueprint, render_template, request, redirect, flash

introduce_blueprint = Blueprint('introduce', __name__)


@introduce_blueprint.route("/introduce", methods=["GET"])
def introduce_get():
    return render_template("introduce.html")


@introduce_blueprint.route("/introduce", methods=["POST"])
def introduce_post():
    return render_template("introduce.html")
