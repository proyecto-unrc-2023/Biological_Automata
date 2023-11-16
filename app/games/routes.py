from flask import jsonify, request
from app.games import api
from Schemas.schemas import *
from models.logic.GameController import Game_Mode, Game_State, GameController
from models.logic.Bacterium import *
from flask_restful import Resource
from app.games.Game import Game
from app import db


diccionario = {}

#class Guardar(Resource):
#   def post(self):
#       data = request.get_json()
#       game_data = {
#            '_game_mode':  data.get('_game_mode'),
#            'spawn_bacterium': data.get('spawn_bacterium'),
#            'spawn_other': data.get('spawn_other'),
#            '_cant_bacterium': data.get('_cant_bacterium'),
#            '_cant_other': data.get('_cant_other'),
#
#        }
#
#       game_schema = GameSchema()
#       game = Game(**game_schema.load(game_data))
#       db.session.add(game)
#       db.session.commit()
#
#       return jsonify({'success': 'true'})

#api.add_resource(Guardar, '/guardar')


class SaveConfig(Resource):
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
        frec_other = data.get('frecOther')
        game_mode = data.get('gameMode')
        id = data.get('id')

        game_data = GameController(Game_Mode(game_mode), cant_bact, frec_bact, cant_other, frec_other)
        game_data.set_spawn_bacterium((x_spawn_b, y_spawn_b))
        game_data.set_spawn_other((x_spawn_o, y_spawn_o))
        game_data.start_game()
        config_id = id

        diccionario[config_id] = game_data


        return {"message": "Configuración guardada correctamente"}

api.add_resource(SaveConfig, '/saveConfig')


class RefreshGame(Resource):
    def get(self, game_id):
        game_data = diccionario[game_id]
        game_data.refresh_board()
        game_schema = GameSchema()
        result = game_schema.dump(game_data)
        return jsonify({"games": result})

api.add_resource(RefreshGame, '/refreshgame/<int:game_id>')


class StopGame(Resource):
    def get(self, game_id):
        game_data = diccionario[game_id]
        game_data.stop()
        return {"message": "El juego freno"}

api.add_resource(StopGame, '/stopgame/<int:game_id>')



#game_data = GameController()

#class Games_Resource(Resource):
#    def get(self):
#        game_schema = GameSchema()
#        result = game_schema.dump(game_data)
#        return jsonify({"games": result})
#
#api.add_resource(Games_Resource, '/game')


#class Config_Game(Resource):
#    def options(self):
#        return '', 204
#
#    def post(self):
#        data = request.get_json()
#        x_spawn_b = data.get('xBacterium')
#        y_spawn_b = data.get('yBacterium')
#        x_spawn_o = data.get('xOther')
#        y_spawn_o = data.get('yOther')
#        cant_bact = data.get('cantBact')
#        cant_other = data.get('cantOther')
#        frec_bact = data.get('frecBact')
#        frec_other = data.get('frecOther')
#        game_mode = data.get('gameMode')
#
#        if game_mode == 1:
#            game_data.config(cant_bact, frec_bact, cant_other, frec_other, Game_Mode.ANTIBIOTIC)
#        else:
#            game_data.config(cant_bact, frec_bact, cant_other, frec_other, Game_Mode.BACTERIOPHAGE)
#
#        game_data.set_spawn_bacterium((x_spawn_b, y_spawn_b))
#        game_data.set_spawn_other((x_spawn_o, y_spawn_o))
#
#        game_data.start_game()
#        return {"message": "Configuración guardada correctamente"}
#
#api.add_resource(Config_Game, '/config')


#class Start_Game(Resource):
#    def get(self):
#        game_data.start_game()
#        return {"message": "Se ha iniciado el juego"}
#
#api.add_resource(Start_Game, '/start')


# class Refresh_Game(Resource):
#     def get(self):
#         game_data.refresh_board()
#         game_schema = GameSchema()
#         result = game_schema.dump(game_data)
#         return jsonify({"games": result})

# api.add_resource(Refresh_Game, '/refresh')


# class Stop_Game(Resource):
#     def get(self):
#         game_data.stop()
#         return {"message": "El juego se detuvo"}

# api.add_resource(Stop_Game, '/stop')
