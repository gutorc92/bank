from flask import Blueprint

bp = Blueprint('agency', __name__)

from app.agency import routes