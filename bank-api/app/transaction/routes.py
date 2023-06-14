from datetime import datetime
from app.transaction import bp
# from flask import Blueprint
from flask import request
# from app import db
from app.extensions import db
from app.models.models import Transaction, Account

@bp.route('/', methods=['GET'])
def list():
    data = db.session.query(Transaction).all()
    response = [item.json() for item in data]
    return {"count": len(response), "items": response}

@bp.route('/deposit', methods=['POST'])
def deposit():
    if request.is_json:
        data = request.get_json()
        account = db.session.query(Account).filter(Account.id == data['account']).one()
        new_transaction = Transaction(
            type_of='credit',
            value=data['value'],
            date=datetime.strptime(data['date'], '%d/%m/%Y'),
            account_id=account.id
        )        
        db.session.add(new_transaction)
        db.session.commit()
        return {"message": f"transaction {new_transaction.id} has been created successfully."}
    else:
        return {"error": "The request payload is not in JSON format"}
    
@bp.route('/draw', methods=['POST'])
def draw():
    if request.is_json:
        data = request.get_json()
        account = db.session.query(Account).filter(Account.id == data['account']).one()
        new_transaction = Transaction(
            type_of='charge',
            value=data['value'],
            date=datetime.strptime(data['date'], '%d/%m/%Y'),
            account_id=account.id
        )        
        db.session.add(new_transaction)
        db.session.commit()
        return {"message": f"transaction {new_transaction.id} has been created successfully."}
    else:
        return {"error": "The request payload is not in JSON format"}
    

@bp.route('/transfer', methods=['POST'])
def transfer():
    if request.is_json:
        data = request.get_json()
        account_origin = db.session.query(Account).filter(Account.id == data['account_origin']).one()
        account_receiver = db.session.query(Account).filter(Account.id == data['account_receiver']).one()
        origin_transaction = Transaction(
            type_of='charge',
            value=data['value'],
            date=datetime.strptime(data['date'], '%d/%m/%Y'),
            account_id=account_origin.id
        )
        receiver_transaction = Transaction(
            type_of='credit',
            value=data['value'],
            date=datetime.strptime(data['date'], '%d/%m/%Y'),
            account_id=account_receiver.id
        )       
        db.session.bulk_save_objects([origin_transaction, receiver_transaction])
        db.session.commit()
        return {"message": f"transactions has been created successfully."}
    else:
        return {"error": "The request payload is not in JSON format"}