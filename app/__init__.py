from flask import Flask
from config import config
from flask_cors import CORS

def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    config[config_name].init_app(app)
    CORS(app)
    return app
