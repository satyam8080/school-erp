from app import app, db
from models.student import Student
from models.tc import Tc


@app.route('/get-tc/<int:id>', methods=['GET'])
def get_tc(id):
    student = Student.query.filter_by(id=id).first()

    if not student:
        return {"message": "Invalid student id"}, 404

    res = []
    tc = Tc.query.filter_by(student_id=id).first()

    if tc:
        if tc.tc_count > 3:
            return {"message": "Maximum limit of TC allocation reached"}, 404

        res = []
        c = tc.tc_count
        tc.tc_count = c + 1
        db.session.commit()

    else:
        tc_store = Tc(student_id=id)
        db.session.add(tc_store)
        db.session.commit()

    obj = {"id": student.id, "name": student.name, "gender": student.gender, "class": student.student_class,
           "section": student.section, "mobile": student.mobile, "father_name": student.father_name,
           "address": student.address, "photo": student.photo, "dob": student.dob,
           "registration_date": student.created_at}
    res.append(obj)
    return {"message": res}, 200
