from flask import Flask

app = Flask(__name__)

from app.controllers import api_controller, view_controller
