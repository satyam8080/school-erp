from app import db
from enum import IntEnum
from datetime import date

class Status(IntEnum):
    ABSENT = 0
    HALF_DAY = 1
    PRESENT = 2


class Attendance(db.Model):
    __tablename__ = "attendance"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    date = db.Column(db.Date, default=date.today, nullable=False)
    status = db.Column(db.Enum(Status), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), index=True, nullable=False)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
