from flask import request
from app import app, db
from werkzeug.utils import secure_filename
import os

@app.route('assignment', methods=['POST'])
def assign():
    question = request.form.get('question', None)
    file = request.form.get('file', None)
    due_date = request.form.get('due_date', None)

    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER_ASSIGNMENT'], filename))
    else:
        filename = None

