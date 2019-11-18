from datetime import datetime
from config import db

class Scores(db.Model):
    __tablename__ = 'scores'
    gameNumber = db.Column(db.Integer, primary_key=True)
    gameDate = db.Column(db.String)
    Dan = db.Column(db.Integer)
    Will = db.Column(db.Integer)
    Ben = db.Column(db.Integer)
    Sven = db.Column(db.Integer)