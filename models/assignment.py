from app import db
from datetime import datetime, timedelta

def get_due_date(self):
      return datetime.utcnow() + timedelta(days=2)


class Assignment(db.Model):
    __tablename__ = 'assignments'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    assignment_file = db.Column(db.String(512), nullable=True)
    comment = db.Column(db.String(512), nullable=True)
    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    due_date = db.Column(db.DateTime, default=get_due_date, nullable=False)

    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), index=True, nullable=False)
    # assignment_id = db.Column(db.Integer, index=True, nullable=False)     

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

