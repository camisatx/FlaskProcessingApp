from flask import Blueprint

bp = Blueprint('api.v1', __name__)

# NOTE: Add extra blueprint routes to this import list
from api.v1 import planes
