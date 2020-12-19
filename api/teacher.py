import os

from werkzeug.utils import secure_filename

from app import app, db
from flask import request
from datetime import date
from models.teacher import Teacher
from models.classes import Classes


@app.route('/teachers', methods=['POST'])
def store_teacher():
    name = request.form.get('name', None)
    gender = request.form.get('gender', None)
    mobile = request.form.get('mobile', None)
    father_name = request.form.get('father_name', None)
    address = request.form.get('address', None)
    photo = request.files.get('photo', None)
    dob = request.form.get('dob', None)

    if not all((name, gender, mobile, address, dob)):
        return {"message": "All fields are required"}, 404
    else:
        if photo:
            photo_filename = secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER_TEACHER_DP'], photo_filename))
        else:
            photo_filename = None

        year, month, day = dob.split('-')
        dob = date(int(year), int(month), int(day))

        teacher_obj = Teacher(name=name, gender=gender, mobile=mobile, father_name=father_name, address=address,
                              photo=photo_filename, dob=dob)
        db.session.add(teacher_obj)
        db.session.commit()

        return {"message": "Teacher created successfully"}, 201


@app.route('/teachers', methods=['GET'])
def get_teacher():
    teachers = Teacher.query.all()
    res = []

    if teachers:
        for teacher in teachers:
            if teacher.photo:
                file_path = 'static/' + os.path.join(app.config['UPLOAD_FOLDER_TEACHER_DP']) + '/' + teacher.photo
            else:
                file_path = None
            obj = {"name": teacher.name, "gender": teacher.gender, "mobile": teacher.mobile, "address": teacher.address,
                   "father_name": teacher.father_name, "photo": file_path, "dob": teacher.dob}
            res.append(obj)
        return {"message": res}, 200
    else:
        return {"message": "No teachers registered yet"}, 200


@app.route('/teachers/<int:id>', methods=['GET'])
def get_teacher_by_id(id):
    teachers = Teacher.query.filter_by(id=id)
    res = []

    if teachers:
        for teacher in teachers:
            if teacher.photo:
                file_path = 'static/' + os.path.join(app.config['UPLOAD_FOLDER_TEACHER_DP']) + '/' + teacher.photo
            else:
                file_path = None
            obj = {"name": teacher.name, "gender": teacher.gender, "mobile": teacher.mobile, "address": teacher.address,
                   "father_name": teacher.father_name, "photo": file_path, "dob": teacher.dob}
            res.append(obj)
        return {"message": res}, 200
    else:
        return {"message": "No teachers registered yet"}, 200


@app.route('/assign-class', methods=['POST'])
def assign_class():
    teacher_id = request.form.get('teacher_id', None)
    class_id = request.form.get('class_id', None)

    if not all((teacher_id, class_id)):
        return {"message": "All fields are required"}, 404
    else:
        class_obj = Classes.query.filter_by(id=class_id)
        flag = 0

        if class_obj:
            for cls in class_obj:
                if cls.teacher_id:
                    flag += flag + 1
                else:
                    pass

            if flag == 0:
                class_obj.teacher_id = teacher_id
                db.session.add(class_obj)
                db.session.commit()
                return {"message": "Teacher assigned"}, 200
            else:
                return {"message": "Another teacher already present in this class"}, 404

        else:
            return {"message": "Invalid class"}, 404