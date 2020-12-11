from datetime import date
from flask import request, jsonify, url_for
from app import app, db
from werkzeug.utils import secure_filename
import os
from models.assignment import Assignment

@app.route('/assignment', methods=['POST'])
def assign():
    question = request.form.get('question', None)
    file = request.files.get('file', None)
    due_date = request.form.get('due_date', None)

    year, month, day = due_date.split('-')
    today = date(int(year), int(month), int(day))

    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER_ASSIGNMENT'], filename))
    else:
        filename = None

    assignment = Assignment(file=filename, text=question, due_date=today)
    db.session.add(assignment)
    db.session.commit()

    return {"message": "Assignment stored successfully"}, 200


@app.route('/assignment', methods=['GET'])
def get_assignment():
    assignments = Assignment.query.all()
    res = []
    for assignment in assignments:
        if assignment.file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER_ASSIGNMENT']) + '/' + assignment.file
        else:
            file_path = None

        obj = {'id': assignment.id, 'question': assignment.text, 'due_date': assignment.due_date,
               'file': file_path}
        res.append(obj)
    return {"message": res}, 200
