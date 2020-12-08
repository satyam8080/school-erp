from flask import request
from app import app, db
from models.attendance import Attendance, Status


# @app.route('/attendance', methods=['GET'])
# def records():

def save_record(records):
    rows = []
    for roll_no, s in records.items():
        record = Attendance(student_id=int(roll_no), status=Status(s))
        rows.append(record)
    db.session.bulk_save_objects(rows)
    db.session.commit()


@app.route('/attendance', methods=['POST'])
def create_record():
    records = request.get_json()
    save_record(records)
    return {"message": "Student records saved"}, 201
