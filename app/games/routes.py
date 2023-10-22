from flask import jsonify, request
from app.games import api
from Schemas.schemas import *
from models.logic.GameController import *
from models.logic.Bacterium import *
from flask_restful import Resource
from app.games.Game import Game
from app import db

#class Game_Resource(Resource):
#    def get(self, game_id):
#        # Obtén los datos del juego desde tu controlador o base de datos
#        game = Game.query.filter_by(id=game_id).first()
#
#
#        if game is None:
#            return jsonify({"error": "Juego no encontrado"})
#
#        # Serializa los datos del juego utilizando el esquema GameSchema
#        game_schema = GameSchema()
#
#        return jsonify(game_schema.dump(game))
#
#api.add_resource(Game_Resource, '/game/<int:game_id>')

game_data = GameController()

class Games_Resource(Resource):
    def get(self):
        game_schema = GameSchema()
        result = game_schema.dump(game_data)
        return jsonify({"games": result})

api.add_resource(Games_Resource, '/game')


class Config_Game(Resource):
    def options(self):
        return '', 204

    def post(self):
        data = request.get_json()
        x_spawn_b = data.get('xBacterium')
        y_spawn_b = data.get('yBacterium')
        x_spawn_o = data.get('xOther')
        y_spawn_o = data.get('yOther')
        cant_bact = data.get('cantBact')
        cant_other = data.get('cantOther')
        frec_bact = data.get('frecBact')
        frec_other = data.get('frecOther')
        game_mode = data.get('gameMode')

        game_data.config(cant_bact, frec_bact, cant_other, frec_other)
        game_data.set_spawn_bacterium((x_spawn_b, y_spawn_b))
        game_data.set_spawn_other((x_spawn_o, y_spawn_o))
        game_data._game_mode = Game_Mode.ANTIBIOTIC if game_mode == 1 else Game_Mode.BACTERIOPHAGE

        game_data.start_game()
        return {"message": "Configuración guardada correctamente"}

api.add_resource(Config_Game, '/config')



class Stop_Game(Resource):
    def get(self):
        game_data.stop()
        return {"message": "El juego se detuvo"}

api.add_resource(Stop_Game, '/stop')



class Refresh_Game(Resource):
    def get(self):
        game_data.refresh_board()
        game_schema = GameSchema()
        result = game_schema.dump(game_data)
        return jsonify({"games": result})

api.add_resource(Refresh_Game, '/refresh')


