from flask import request

from app import app
from models.enquiry import Enquiry


@app.route('/enquiry', methods=['POST'])
def enquiry():
    student_name = request.form.get('name', None)
    address = request.form.get('address', None)
    father_name = request.form.get('father_name', None)
    interested_class = request.form.get('class', None)
    mobile = request.form.get('mobile', None)

    if not all((student_name, address, father_name, interested_class, mobile)):
        return {"message": "a required property is missing"}, 404

    enquiry_form = Enquiry(student_name=student_name, address=address,
                           father_name=father_name, interested_class=interested_class, mobile=mobile)
    enquiry_form.save_to_db()
    return {"message": "enquiry form saved successfully"}, 201


@app.route('/enquiry', methods=['GET'])
def enquiry_get():
    date_form = request.form.get('date', None)
    res = []

    if date_form:
        date_form = date_form + '%'
        data = Enquiry.query.filter(Enquiry.date.like(date_form)).all()
        for da in data:
            obj = {"student_name": da.student_name, "address": da.address, "father_name": da.father_name,
                   "interested_class": da.interested_class, "mobile": da.mobile}
            res.append(obj)
        return {"data": res}, 200
    else:
        data = Enquiry.query.all()
        for da in data:
            obj = {"student_name": da.student_name, "address": da.address, "father_name": da.father_name,
                   "interested_class": da.interested_class, "mobile": da.mobile }
            res.append(obj)
        return {"data": res}, 200

