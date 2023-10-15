from flask import Blueprint, render_template, request

views = Blueprint(__name__, "views")


@views.route("/", methods=["get", "post"])
def t2p():
    parameters = request.form.to_dict(flat=True)
    print(parameters)
    return render_template("T2P.html", data=parameters)


@views.route("/results", methods=["get", "post"])
def results():
    return render_template("results.html", benefits="3000")
