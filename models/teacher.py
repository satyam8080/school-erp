from datetime import datetime
from enum import Enum

from app import db


class GenderType(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHER = "OTHER"


class Teacher(db.Model):
    __tablename__ = 'teachers'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(256), nullable=False)
    gender = db.Column(db.Enum(GenderType), nullable=False)
    mobile = db.Column(db.String(32), nullable=False)
    father_name = db.Column(db.String(256), nullable=True)
    address = db.Column(db.String(512), nullable=False)
    photo = db.Column(db.String(512), nullable=True)
    dob = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
