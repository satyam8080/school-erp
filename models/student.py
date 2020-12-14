from app import db
from datetime import datetime
from enum import Enum


class GenderType(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHER = "OTHER"


class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(256), nullable=False)
    gender = db.Column(db.Enum(GenderType), nullable=False)
    student_class = db.Column(db.String(32), nullable=False)
    section = db.Column(db.String(6), nullable=True)
    mobile = db.Column(db.String(32), nullable=False)
    father_name = db.Column(db.String(256), nullable=True)
    address = db.Column(db.String(512), nullable=False)
    tc = db.Column(db.String(512), nullable=True)
    photo = db.Column(db.String(512), nullable=True)
    migration = db.Column(db.String(512), nullable=True)
    dob = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
