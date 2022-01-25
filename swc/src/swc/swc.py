import os
import sys
import traceback

from flask import Flask
from flasgger import Swagger
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from routes import init_route
from utils.app_setup import load_conf
from utils.app_setup import setup_logging

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Initialize the app
app = Flask(__name__, static_url_path='/static')
swagger = Swagger(app)
db = SQLAlchemy(app)
migrate = Migrate(app,db)

SECRET_KEY = "1ULFNxP+a3&[cN[8^7Kh1"
app.secret_key = "1ULFNxP+a3&[cN[8^7Kh1"
app.config.from_object(__name__)

api = Api(app)
app.environment = "DEV"
app.debug = True


def init_app(app):
    try:
        # Load settings
        # load_conf(app)
        # setup_logging(app)
        init_db(app)
        init_route(app, api)
        app.logger.info('SWC application initialized.')
    except:
        app.logger.error(traceback.format_exc())


# TODO Add DB Configuration here..
def init_db(app):
    try:
        app.config['SQLALCHEMY_DATABASE_URI'] = "postgersql://postgres:1148@localhost:5432/flask"
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        # app.modelgpt2 = GPT2Model()
        # app.modelgpt2 = torch.load('models/model_gpt2.pt', map_location=torch.device('cpu'))
        # app.modelgpt2tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
        # print("GPT2 Model Loaded..")
        app.dbhostname = "0.0.0.0"

    except:
        app.logger.error(traceback.format_exc())


init_app(app)
