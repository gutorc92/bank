from app.person import bp
# from flask import Blueprint
from flask import request
# from app import db
from app.extensions import db
from app.models.models import Person

@bp.route('/', methods=['GET'])
def list_tickets():
    persons = db.session.query(Person).all()
    response = [person.json() for person in persons]
    return {"count": len(response), "items": response}

@bp.route('/', methods=['POST'])
def ticket_list():
    if request.is_json:
        data = request.get_json()
        new_person = Person(
            name=data['name'],
            surname=data['surname'],
            id_gov=data['id_gov']
        )
        
        db.session.add(new_person)
        db.session.commit()
        return {"message": f"ticket {new_person.id} has been created successfully."}
    else:
        return {"error": "The request payload is not in JSON format"}