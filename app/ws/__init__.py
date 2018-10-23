from flask import Blueprint

bp = Blueprint('ws', __name__)

from app.ws import routes
