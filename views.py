from flask import Blueprint, render_template

views = Blueprint(__name__, "views")


@views.route("/")
def t2p():
    return render_template("T2P.html")
