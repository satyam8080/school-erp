from app import db
from datetime import datetime


class Enquiry(db.Model):
    __tablename__ = 'enquiry'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_name = db.Column(db.String(512), nullable=False)
    address = db.Column(db.String(512), nullable=False)
    mobile = db.Column(db.String(32), nullable=False)
    father_name = db.Column(db.String(512), nullable=False)
    interested_class = db.Column(db.String(512), nullable=True)
    date = db.Column(db.DateTime, default=datetime.now, nullable=False)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
