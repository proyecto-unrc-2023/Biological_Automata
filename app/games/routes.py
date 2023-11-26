from flask import jsonify, request, session
from app.games import api
from Schemas.schemas import *
from models.logic.GameController import GameController
from models.logic.Game_Mode import Game_Mode
from models.logic.Game_State import Game_State
from models.logic.Bacterium import *
from flask_restful import Resource
from app.games.User import User
from app import db


diccionario = {}

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
        if cant_bact < 0 or cant_other < 0:
            return {"message": "Las cantidades que salen del spawn no pueden ser negativas!"}
        if frec_bact <= 0 or frec_other <= 0:
            return {"message": "Las frecuencias deben ser positivas!"}

        game_data = GameController(Game_Mode(game_mode), cant_bact, frec_bact, cant_other, frec_other)
        game_data.set_spawn_bacterium((x_spawn_b, y_spawn_b))
        game_data.set_spawn_other((x_spawn_o, y_spawn_o))


        moves_reproduction = data.get('movesReproduction')
        moves_recovery = data.get('movesRecovery')
        power_antibiotic = data.get('powerAntibiotic')
        moves_explotion = data.get('movesExplotion')
        virus_after_explotion = data.get('virusAfterExplotion')
        initial_power_infection = data.get('initialPowerInfection')
        mutation_probability = data.get('mutationProbability')
        cant_overpopulation = data.get('cantOverpopulation')

        if moves_reproduction <= 0 or moves_recovery <= 0 or moves_explotion <= 0:
            return {"message": "Los movimientos deben ser positivos"}
        if power_antibiotic <= 0 or virus_after_explotion <= 0 or initial_power_infection <= 0:
            return {"message": "Los valores iniciales para los antibioticos y bacteriofagos deben ser positivos!"}
        if mutation_probability < 0 or mutation_probability > 1:
            return {"message": "La probabilidad de mutacion debe estar entre 0 y 1"}
        if cant_overpopulation <= 1:
            return {"message": "La cantidad para sobrepoblación debe ser mayor a 1!"}

        game_data.advanced_config(moves_reproduction, moves_recovery, power_antibiotic,
                                 moves_explotion, virus_after_explotion, initial_power_infection,
                                 mutation_probability, cant_overpopulation)
        game_data.start_game()
        if id in diccionario:
            del diccionario[id]

        diccionario[id] = game_data

        return {"id": id, "message": "Configuración guardada correctamente"}

class RefreshGame(Resource):
    def get(self, game_id):

        game_data = diccionario.get(game_id)

        if game_data is None:
            return {"message": "ID de juego no encontrado"}, 401

        if game_data._game_state == Game_State.FINISHED:
            return {"message": "Juego Terminado"}, 404


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

        gameState = game_data._game_state
        if gameState != Game_State.START_GAME or gameState != Game_State.FINISHED:
            return {"message": "El juego no esta EMPEZADO O TERMINADO"}
        game_data.stop()
        return {"message": "El juego freno"}


##Usuarios
class RegisterUser(Resource):
    def options(self):
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


api.add_resource(New_Game, '/newgame')
api.add_resource(RefreshGame, '/refreshgame/<string:game_id>')
api.add_resource(StopGame, '/stopgame/<string:game_id>')
