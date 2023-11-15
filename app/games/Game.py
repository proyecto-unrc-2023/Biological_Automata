from marshmallow import Schema, fields
from Schemas.schemas import *
from models.logic.GameController import *
from app import db
import json

class Game(db.Model):
    __tablename__ = 'game'
    id = db.Column(db.Integer, primary_key=True)
    _game_mode = db.Column(db.Text)
    spawn_bacterium = db.Column(db.Text)
    spawn_other = db.Column(db.Text)
    _cant_bacterium = db.Column(db.Integer)
    _cant_other = db.Column(db.Integer)
    _board = db.Column(db.Text, nullable=False)

    def __init__(self, _game_mode, spawn_bacterium, spawn_other, _cant_bacterium, _cant_other):
      self._game_mode = _game_mode
      self.spawn_bacterium = spawn_bacterium
      self.spawn_other = spawn_other
      self._cant_bacterium = _cant_bacterium
      self._cant_other = _cant_other

      game_data = GameController()
      game_data.config(_cant_bacterium, 20, _cant_other, 10, Game_Mode.ANTIBIOTIC)
      game_data.set_spawn_bacterium((spawn_bacterium[0], spawn_bacterium[1]))
      game_data.set_spawn_other((spawn_other[0], spawn_other[1]))
      board_schema = BoardSchema()
      result = board_schema.dump(game_data._board)
      self._board = result

    # def __init__(self, name):
    #     self.name = name
    #     game = GameController()
    #     game_schema = GameSchema()
    #     result = game_schema.dump(game)
    #     self.board = json.dumps({
    #         "board": result
    #     })

    def json(self):
        return {
            'id': self.id,
            '_board': self._board
        }



