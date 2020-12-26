from app import db
from datetime import datetime


class Tc(db.Model):
    __tablename__ = 'tc'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), index=True, nullable=True)
    tc_count = db.Column(db.Integer, default=0, nullable=True)
    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
