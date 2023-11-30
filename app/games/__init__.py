from flask import Blueprint
from flask_restful import Api
from models.logic.GameController import *
from Schemas.schemas import *

games_bp = Blueprint('games', __name__)
api = Api(games_bp)

from app.games import routes
from app.games import User
