from flask import jsonify, request, session
from app.games import api
from Schemas.schemas import *
from models.logic.GameController import GameController
from models.logic.Game_Mode import Game_Mode
from models.logic.Bacterium import *
from flask_restful import Resource
from app.games.User import User
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


class New_Game(Resource):
    def options(self):
        return '', 204

    def post(self):
        # if not session.get("user_id"):
        #     return {"message": "Usuario no autenticado"}, 401

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

class RefreshGame(Resource):
    def get(self, game_id):
        # if not session.get("user_id"):
        #     return {"message": "Usuario no autenticado"}, 401

        game_data = diccionario.get(game_id)

        if game_data is None:
            return {"message": "ID de juego no encontrado"}, 404

        game_data.refresh_board()
        game_schema = GameSchema()
        result = game_schema.dump(game_data)
        return jsonify({"games": result})

class StopGame(Resource):
    def get(self, game_id):
        # if not session.get("user_id"):
        #     return {"message": "Usuario no autenticado"}, 401

        game_data = diccionario[game_id]

        if game_data is None:
            return {"message": "ID de juego no encontrado"}, 404

        game_data.stop()
        return {"message": "El juego freno"}


##Usuarios
class RegisterUser(Resource):
    def options(self):
        if session.get("user_id"):
            return {"message": "Ya se tiene un inicio de session de usuario"}, 401
        return '', 204

    def post(self):
        data = request.get_json()
        nickname = data.get('nickname')
        email = data.get('email')
        password = data.get('password')
        repPassword = data.get('repPassword')

        if (password != repPassword):
            return {"message": "Contraseñas no coinciden"},401

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return {"message": "El email ya está en uso"},401

        existing_user = User.query.filter_by(nickname=nickname).first()
        if existing_user:
            return {"message": "El nickname ya está en uso"},401


        user = User(nickname, email, password)
        user.save_to_db()
        return {"message": "Usuario Registrado con Exito"}

class LoginUser(Resource):
    def post(self):
        data = request.get_json()
        nickname = data.get('nickname')
        password = data.get('password')

        user = User.query.filter_by(nickname=nickname).first()

        if not user or not user.check_password(password):
            return {"message": "Datos invalidos"}, 401

        session['user_id'] = user.id
        return {
            "message": "Inicio de sesión exitoso",
            "user": {
                "id": user.id,
                "nickname": user.nickname,
                }
            }


class Logout(Resource):
    def get(self):
        # if not session.get("user_id"):
        #     return {"message": "Usuario no autenticado"}, 401

        session["user_id"] = None
        return {"message": "Se ha cerrado session con exito"}


api.add_resource(RegisterUser, '/register')
api.add_resource(LoginUser, '/login')
api.add_resource(Logout, '/logout')


api.add_resource(New_Game, '/saveConfig')
api.add_resource(RefreshGame, '/refreshgame/<int:game_id>')
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
