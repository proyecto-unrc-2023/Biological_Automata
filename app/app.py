from flask import Flask, Blueprint, render_template, jsonify
from app import create_app
import os

from Schemas.schemas import *
from models.logic.cell import Cell
from models.logic.board import Board
from models.logic.Bacterium import *
from models.logic.Bacteriophage import Bacteriophage
from models.logic.GameController import GameController

#app = create_app(os.getenv('FLASK_CONFIG') or 'default')  ##esto no anda
game_bp = Blueprint('game_bp', __name__)
app = Flask(__name__)


@app.route('/')
def index():
    return "hola"


@app.route('/bacterium', methods=['GET'])
def get_bacterium():
    # Creo una insancia de bacteria
    bacterium_instance = Bacterium(moves=1)

    # esto es para serializar con BacteriumSchema
    bacterium_schema = BacteriumSchema()
    result = bacterium_schema.dump(bacterium_instance)

    # devuelvo la serializacion en formato de json
    return jsonify(result), 200



@app.route('/bacteriophage', methods=['GET'])
def get_bacteriophage():
    # Crear una instancia de Bacteriophage
    bacteriophage_instance = Bacteriophage(5)

      # Serializar la instancia utilizando el esquema BacteriophageSchema
    bacteriophage_schema = BacteriophageSchema()
    result = bacteriophage_schema.dump(bacteriophage_instance)
    # Devolver la instancia serializada en formato JSON
    return jsonify(result), 200




@app.route('/cell', methods=['GET'])
def get_cell():

    cell_instance = Cell()
    cell_instance.set_spawn_bacterium()
    cell_schema = CellSchema()
    result = cell_schema.dump(cell_instance)

    # Devolver la instancia serializada en formato JSON
    return jsonify(result), 200



@app.route('/board', methods=['GET'])
def get_board():

    board = Board(4,4)
    cell_instance = Cell()
    cell_instance.add_antibiotic()
    cell_instance.add_bacterium(0,'b')
    cell_instance.add_bacteriophage(4)
    board.put_celda(1,1,cell_instance)
    board_schema = BoardSchema()
    result = board_schema.dump(board)

    # Devolver la instancia serializada en formato JSON
    return jsonify(result), 200

@app.route('/juego', methods=['GET'])
def get_game():
    game = GameController()
    game.config(2,2)
    game_schema = GameSchema()
    result = game_schema.dump(game)

    # Devolver la instancia serializada en formato JSON
    return jsonify(result), 200


if __name__ == '__main__':
  app.run(debug=True)


#request es un objeto proporcionado por FLASK que contiene informacion de la solicitud HTTP.

#La función render_template se encarga de combinar tus plantillas HTML con los datos que
# le proporcionas desde tu código Python, para luego generar una página HTML completa que será enviada
# al navegador del usuario.
