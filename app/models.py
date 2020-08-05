from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Thing(db.Model):
    __tablename__ = "things"
    id = db.Column(db.Integer, primary_key=True)
    thing = db.Column(db.String, nullable=False)
