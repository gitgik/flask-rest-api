# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# local import
from instance.config import app_config

# initialize db
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    return app
