from flask import request
from app import app
from models.fee_transaction import FeeTransaction


@app.route('/fee-transaction', methods=['POST'])
def create_fee_transaction():
    amount = request.form.get('amount', None)
    session = request.form.get('session', None)
    student_id = request.form.get('student_id', None)
    transaction_id = request.form.get('transaction_id', None)
    mode = request.form.get('mode', None)
    months = request.form.get('months', None)
    data = FeeTransaction(amount=amount, session=session, student_id=student_id, transaction_id=transaction_id,
                          mode=mode, months=months)
    data.save_to_db()
    return {"message": "successfully"}, 201


@app.route('/fee-transaction/<int:id>', methods=['GET'])
def get_fee_transaction(id):
    transactions = FeeTransaction.query.filter_by(student_id=id).all()
    fee_record = []
    for t in transactions:
        obj = {'session': t.session, 'student_id': t.student_id, 'amount': t.amount,
               'transaction_date': t.transaction_date, 'transaction_id': t.transaction_id, 'mode': t.mode,
               'months': t.months}
        fee_record.append(obj)
    return {"fee-record": fee_record}, 200
