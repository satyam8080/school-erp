from app import db
from datetime import datetime


class Classes(db.Model):
    __tablename__ = 'Classes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(6), nullable=True)
    section = db.Column(db.String(3), nullable=True) 
    date = db.Column(db.DateTime, default=datatime.utcnow, nullable=False)  

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

