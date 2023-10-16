import os
from app import create_app
from app import db

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

if __name__ == '__main__':
    app.run(debug=True)

    with app.app_context():
        db.create_all()
        for rule in app.url_map.iter_rules():
            print(rule)


#@app.route('/')
#def index():
#    return "hola"
#
#
#@app.route('/bacterium', methods=['GET'])
#def get_bacterium():
#    # Creo una insancia de bacteria
#    bacterium_instance = BacteriumNormal(moves=1)
#
#    # esto es para serializar con BacteriumSchema
#    bacterium_schema = BacteriumSchema()
#    result = bacterium_schema.dump(bacterium_instance)
#
#    # devuelvo la serializacion en formato de json
#    return jsonify(result), 200
#
#
#
#@app.route('/bacteriophage', methods=['GET'])
#def get_bacteriophage():
#    # Crear una instancia de Bacteriophage
#    bacteriophage_instance = Bacteriophage(5)
#
#      # Serializar la instancia utilizando el esquema BacteriophageSchema
#    bacteriophage_schema = BacteriophageSchema()
#    result = bacteriophage_schema.dump(bacteriophage_instance)
#    # Devolver la instancia serializada en formato JSON
#    return jsonify(result), 200
#
##
#
#
#@app.route('/cell', methods=['GET'])
#def get_cell():
#
#    cell_instance = Cell()
#    cell_instance.set_spawn_bacterium()
#    cell_instance.add_bacterium(1, 'b')
#    cell_instance.add_bacterium(1, 'd')
#    cell_instance.add_bacterium(1, 'f')
#    cell_schema = CellSchema()
#    result = cell_schema.dump(cell_instance)
#
#    # Devolver la instancia serializada en formato JSON
#    return jsonify(result), 200

#
#
#@app.route('/board', methods=['GET'])
#def get_board():
#    board = Board(4,4)
#    cell_instance = Cell()
#    cell_instance.add_antibiotic()
#    cell_instance.add_bacterium(0,'b')
#    cell_instance.add_bacteriophage(4)
#    board.put_celda(1,1,cell_instance)
#    board_schema = BoardSchema()
#    result = board_schema.dump(board)
#
#    # Devolver la instancia serializada en formato JSON
#    return jsonify(result), 200
#
#@app.route('/juego', methods=['GET'])
#def get_game():
#    game = GameController()
#    game_schema = GameSchema()
#    result = game_schema.dump(game)
#
#    # Devolver la instancia serializada en formato JSON
#    return jsonify(result), 200
#


#request es un objeto proporcionado por FLASK que contiene informacion de la solicitud HTTP.

#La función render_template se encarga de combinar tus plantillas HTML con los datos que
# le proporcionas desde tu código Python, para luego generar una página HTML completa que será enviada
# al navegador del usuario.
