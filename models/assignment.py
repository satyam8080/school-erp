from app import db
from datetime import datetime, timedelta


def get_due_date():
    return datetime.utcnow() + timedelta(days=2)


class Assignment(db.Model):
    __tablename__ = 'assignments'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    file = db.Column(db.String(512), nullable=True)
    text = db.Column(db.String(5000), nullable=True)
    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    due_date = db.Column(db.DateTime, default=get_due_date, nullable=False)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

