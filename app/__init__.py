from flask import Flask
from config import config
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(session_options={"expire_on_commit": False})


def create_app(config_name='development'):
    app = Flask(__name__)
    CORS(app)
    register_modules(app)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    return app


def register_modules(app):
    from app.games import games_bp
    app.register_blueprint(games_bp, url_prefix='/game')
