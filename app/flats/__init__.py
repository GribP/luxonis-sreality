from flask import Blueprint

bp = Blueprint('flats', __name__)


from app.flats import routes
