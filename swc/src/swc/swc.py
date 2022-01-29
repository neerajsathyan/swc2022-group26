import os
import sys
import traceback

from flask import Flask
from flasgger import Swagger
from flask_restful import Api
from flask_cors import CORS

from apis.psql_models import db

from flask_cors import CORS

from routes import init_route
from utils.app_setup import load_conf
from utils.app_setup import setup_logging

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
# Initialize the app
app = Flask(__name__, static_url_path='/static')
CORS(app)
swagger = Swagger(app)

SECRET_KEY = "1ULFNxP+a3&[cN[8^7Kh1"
app.secret_key = "1ULFNxP+a3&[cN[8^7Kh1"
app.config.from_json("conf/conf.json")

api = Api(app)
app.environment = "DEV"
app.debug = True


def init_app(app):
    try:
        # Load settings
        # load_conf(app)
        setup_logging(app)
        init_db(app)
        CORS(app)
        init_route(app, api)
        app.logger.info('SWC application initialized.')
    except:
        app.logger.error(traceback.format_exc())


def init_db(app):
    try:
        db.init_app(app)

    except:
        app.logger.error(traceback.format_exc())


init_app(app)
