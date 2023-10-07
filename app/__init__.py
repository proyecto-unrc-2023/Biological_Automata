from flask import Flask
from config import config
from flask_cors import CORS

def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    config[config_name].init_app(app)
    CORS(app)
    register_modules(app)
    return app

def register_modules(app):
    from .games import games_bp
    app.register_blueprint(games_bp, url_prefix='/games')
