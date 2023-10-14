from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/static")
def style():
    return url_for("static", filename="style.css")


if __name__ == "__main__":
    app.run()
