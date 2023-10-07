from flask import jsonify, request
from app.games import api
from models.Schemas.schemas import GameSchema

from flask_restful import Resource

class GamesResource(Resource):
    def get(self):
        game_data = []
        game_schema = GameSchema()


class GameResource(Resource):
    def get(self, game_id):
        return jsonify(game_schema.dump(game))

    def post(self):

        return jsonify({'success': 'true'})

    def index(self):
        return jsonify({"success": "false"})

api.add_resource(GameResource, '/', '/<int:game_id>', '/')
api.add_resource(GamesResource, '/index')
