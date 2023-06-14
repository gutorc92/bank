from app.agency import bp
# from flask import Blueprint
from flask import request
# from app import db
from app.extensions import db
from app.models.models import Agency

@bp.route('/', methods=['GET'])
def list_agency():
    persons = db.session.query(Agency).all()
    response = [person.json() for person in persons]
    return {"count": len(response), "items": response}

@bp.route('/', methods=['POST'])
def create_agency():
    if request.is_json:
        data = request.get_json()
        new_agency = Agency(
            bc_identify=data['bc_identify'],
            city=data['city'],
        )
        
        db.session.add(new_agency)
        db.session.commit()
        return {"message": f"ticket {new_agency.id} has been created successfully."}
    else:
        return {"error": "The request payload is not in JSON format"}