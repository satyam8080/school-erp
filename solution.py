from flask import request
from app import app
from werkzeug.utils import secure_filename
import os
from models.solution import Solution

ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/solution', methods=['POST'])
def submit_homework():
    student_id = request.form.get('student_id', None)
    assignment_id = request.form.get('assignment_id', None)
    solution_file = request.files.get('solution_file', None)
    comment = request.form.get('comment', None)

    if solution_file:
        solution_filename = secure_filename(solution_file.filename)
        solution_file.save(os.path.join(app.config['UPLOAD_FOLDER_SOLUTION'], solution_filename))
    else:
        solution_filename = None

    solution = Solution(solution_file=solution_filename, student_id=student_id,
                        comment=comment, assignment_id=assignment_id)

    solution.save_to_db()
    return {'message': 'Student solution saved successfully'}, 201

