from app import db
from datetime import datetime


class FeeTransaction(db.Model):
    __tablename__ = 'fee_transactions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), index=True, nullable=False)
    amount = db.Column(db.Integer, nullable=True)
    session = db.Column(db.String(10), nullable=False)
    transaction_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    transaction_id = db.Column(db.String(255), nullable=False)
    mode = db.Column(db.String(64), nullable=False)
    months = db.Column(db.String(64), nullable=False)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

