from app import app
from flask import request
from models.enquiry import Enquiry

@app.route('/enquiry', methods=['POST'])
def enquiry():
    student_name = request.form.get('student_name', None)
    address = request.form.get('address', None)
    father_name = request.form.get('father_name', None)
    interested_class = request.form.get('interested_class', None)

    if not all((student_name, address, father_name, interested_class)):
        return {"message": "a required property is missing"}

    enquiry_form = Enquiry(student_name=student_name, address=address,
                           father_name=father_name, interested_class=interested_class)
    enquiry_form.save_to_db()
    return {"message": "enquiry form saved successfully"}, 201

