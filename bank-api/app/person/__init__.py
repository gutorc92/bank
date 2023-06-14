from flask import Blueprint

bp = Blueprint('person', __name__)

from app.person import routes