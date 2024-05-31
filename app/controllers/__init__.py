from flask import Blueprint

api_bp = Blueprint('api', __name__)
view_bp = Blueprint('view', __name__)

from app.controllers import api_controller, view_controller
