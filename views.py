from flask import Blueprint, render_template, request
from t2p_model import results

views = Blueprint(__name__, "views")


@views.route("/", methods=["get", "post"])
def t2p():
    """
    parameters = request.form.to_dict(flat=True)
    solution = results(parameters)
    """
    return render_template("T2P.html")


@views.route("/results", methods=["get", "post"])
def results():
    return render_template("results.html", benefits="3000")
