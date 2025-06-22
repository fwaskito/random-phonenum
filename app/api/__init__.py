from flask import Blueprint

bp = Blueprint("api", __name__)

from app.api.controllers import main
