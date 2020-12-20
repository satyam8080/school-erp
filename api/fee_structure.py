from flask import request
from app import app
from models.fee_structure import FeeStructure


@app.route('/fee-structure', methods=['POST'])
def create_fee_structure():
    class_name = request.form.get('class_name', None)
    amount = request.form.get('amount', None)
    session = request.form.get('session', None)

    fee_obj = FeeStructure(class_name=class_name, amount=amount, session=session)
    fee_obj.save_to_db()

    return {"message": "fee structure created successfully"}, 200


@app.route('/fee-structure', methods=['GET'])
def get_fee_structure():
    class_name = request.args.get('class_name', None)
    session = request.args.get('session', None)

    if class_name and session:
        all_structures = FeeStructure.query.filter(class_name=class_name, session=session).all()
    elif class_name:
        all_structures = FeeStructure.query.filter(class_name=class_name).all()
    elif session:
        all_structures = FeeStructure.query.filter(session=session).all()
    else:
        all_structures = FeeStructure.query.all()

    return {'data': all_structures}, 200

