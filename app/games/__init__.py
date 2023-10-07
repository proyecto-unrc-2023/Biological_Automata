from flask import Blueprint
from flask_restful import Api
# Create a blueprint
games_bp = Blueprint('games', __name__)
api = Api(games_bp)

from app.games import routes
from app.games import game
