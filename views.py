from flask import Blueprint, render_template, request
import t2p_model

views = Blueprint(__name__, "views")


@views.route("/", methods=["get", "post"])
def t2p():
    parameters = 0
    if request.method == "POST":
        parameters = request.form.to_dict(flat=True)
        print(parameters)
    solution = t2p_model.results(parameters)
    return render_template("T2P.html", data=solution)


@views.route("/results", methods=["get", "post"])
def results():
    return render_template("results.html", benefits="3000")
