from flask import jsonify, request
from app.games import api
from Schemas.schemas import *
from models.logic.GameController import *

from flask_restful import Resource



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
    def post(self, xSpawnB, ySpawnB, xSpawnO, ySpawnO, cant_bact, cant_other, frec_bact, frec_other, gameMode):
        game_data.config(cant_bact,frec_bact,cant_other,frec_other)
        game_data.set_spawn_bacterium((xSpawnB,ySpawnB))
        game_data.set_spawn_other((xSpawnO,ySpawnO))
        if (gameMode == 1):
            game_data._game_mode = Game_Mode.ANTIBIOTIC
        else:
            game_data._game_mode = Game_Mode.BACTERIOPHAGE
        game_data.start_game()
        return {"message": "Configuración guardada correctamente"}

api.add_resource(Config_Game, '/config/<int:xSpawnB>/<int:ySpawnB>/<int:xSpawnO>/<int:ySpawnO>/<int:cant_bact>/<int:cant_other>/<int:frec_bact>/<int:frec_other>/<int:gameMode>')


class Stop_Game(Resource):
    def post(self):
        game_data.stop()
        return {"message": "El juego se detuvo"}

api.add_resource(Stop_Game, '/stop')



class Refresh_Game(Resource):
    def get(self):
        game_data.refresh_board()
        game_schema = GameSchema()
        result = game_schema.dump(game_data)
        return game_data._board.__str__()

api.add_resource(Refresh_Game, '/refresh')
