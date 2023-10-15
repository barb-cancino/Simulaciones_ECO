from flask import Blueprint, render_template

views = Blueprint(__name__, "views")


@views.route("/")
def t2p():
    return render_template("T2P.html")


@views.route("/results")
def results():
    return render_template("results.html", benefits="3000")
