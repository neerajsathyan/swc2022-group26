import os
from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from apis.psql_models import db

app = Flask(__name__)

app.config.from_json("conf/conf.json")
host = os.getenv('POSTGRES_HOST')
port = os.getenv('POSTGRES_PORT')
username = os.getenv('POSTGRES_USER')
dbname = os.getenv('POSTGRES_DB')
password = os.getenv('POSTGRES_PASSWORD')
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{dbname}"
db.init_app(app)

migrate = Migrate(app=app, db=db)
manager = Manager(app=app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()