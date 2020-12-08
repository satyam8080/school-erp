from app import db
from datetime import datetime

class Solution(db.Model):
    __tablename__ = 'solution'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    solution_file = db.Column(db.String(512), nullable=True)
    comment = db.Column(db.String(512), nullable=True)
    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), index=True, nullable=False)
    assignment_id = db.Column(db.Integer, index=True, nullable=False)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

