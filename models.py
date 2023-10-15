from . import db


class Parameters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
