from flask import Blueprint

web_routes = Blueprint('web_routes', __name__)

from .default import *
