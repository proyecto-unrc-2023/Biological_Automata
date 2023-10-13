from flask import jsonify, request
from app.games import api
from Schemas.schemas import *
from models.logic.GameController import *

from flask_restful import Resource


game_data = GameController()
game_data.config(2,2)
game_data.set_spawn_bacterium((1,1))
game_data.set_spawn_other((0,0))

class Games_Resource(Resource):
    def get(self):
        game_data._game_mode = Game_Mode.ANTIBIOTIC
        game_data.refresh_board()
        game_schema = GameSchema()
        result = game_schema.dump(game_data)
        return jsonify({"games": result})

class Game_Resource(Resource):
    def post(self, rows, column):
        game_data = GameController()
        game_data.config(rows, column)
        return {'result': 'hecho correctamente'}

api.add_resource(Games_Resource, '/game')
api.add_resource(Game_Resource, '/game/<int:rows>')

