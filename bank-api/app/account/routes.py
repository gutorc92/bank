from app.account import bp
# from flask import Blueprint
from flask import request
# from app import db
from app.extensions import db
from app.models.models import Account, Person, Agency, Transaction

@bp.route('/', methods=['GET'])
def list():
    data = db.session.query(Account).all()
    response = [item.json() for item in data]
    return {"count": len(response), "items": response}

@bp.route('/<id>/balance', methods=['GET'])
def balance(id):
    if request.method == 'GET':
      account = Account.query.filter_by(id = id).one()
      transactions = Transaction.query.filter_by(account_id = account.id).all()  
      new_account = account.json()
      balance = 0
      for transaction in transactions:
          if transaction.type_of == 'credit':
              balance += transaction.value
          else:
              balance -= transaction.value
      new_account['balance'] = balance
      return {"item": new_account}

@bp.route('/', methods=['POST'])
def create():
    if request.is_json:
        data = request.get_json()
        agency = db.session.query(Agency).filter(Agency.id == data['agency']).one()
        person = db.session.query(Person).filter(Person.id == data['person']).one()
        new_account = Account(
            bc_identify=data['bc_identify'],
            type=data['type'],
        )
        new_account.person_owner = person.id
        new_account.agency_owner = agency.id
        
        db.session.add(new_account)
        db.session.commit()
        return {"message": f"account {new_account.id} has been created successfully."}
    else:
        return {"error": "The request payload is not in JSON format"}