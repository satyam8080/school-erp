from app import app, db
from flask import request
from models.student import Student
from werkzeug.utils import secure_filename
import os
from datetime import date

ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return "Hello World!"


@app.route('/registration', methods=['POST'])
def register_student():
    # print(request.files)
    name = request.form.get('name', None)
    gender = request.form.get('gender', None)
    student_class = request.form.get('student_class', None)
    mobile = request.form.get('mobile', None)
    father_name = request.form.get('father_name', None)
    address = request.form.get('address', None)
    tc = request.files.get('tc', None)
    migration = request.files.get('migration', None)
    photo = request.files.get('photo', None)
    dob = request.form['dob']

    year, month, day = dob.split('-')
    today = date(int(year), int(month), int(day))

    if tc:
        tc_filename = secure_filename(tc.filename)
        tc.save(os.path.join(app.config['UPLOAD_FOLDER_TC'], tc_filename))
    else:
        tc_filename = None

    if migration:
        migration_filename = secure_filename(migration.filename)
        migration.save(os.path.join(app.config['UPLOAD_FOLDER_MIGRATION'], migration_filename))
    else:
        migration_filename = None

    if photo:
        photo_filename = secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER_PHOTO'], photo_filename))
    else:
        photo_filename = None

    if not (name or gender or student_class or mobile or address or dob):
        return {
                   "status": 404,
                   "message": "Missing property"
               }, 404

    else:
        new_student = Student(name=name, gender=gender, student_class=student_class,
                              mobile=mobile, father_name=father_name, address=address,
                              tc=tc_filename, migration=migration_filename, dob=today, photo=photo_filename)
        db.session.add(new_student)
        db.session.commit()

        return {
                   "status": 200,
                   "message": {
                       "student_id": new_student.id
                   }
               }, 200


@app.route('/test', methods=['POST', 'GET'])
def test():
    print(request.form)
    return request.form


@app.route('/students', methods=['GET'])
def get_student_details():
    students = Student.query.all()
    res = []
    if students:
        for student in students:
            obj = {'id': student.id, 'name': student.name}
            res.append(obj)
        return {'students': res}, 200

    else:
        return {"message": "No student"}, 404
