from app import db
from datetime import datetime


class FeeStructure(db.Model):
    __tablename__ = 'fee_structure'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    class_name = db.Column(db.String(6), nullable=True)
    amount = db.Column(db.Integer, nullable=False) 
    session = db.Column(db.String(10), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)  

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

