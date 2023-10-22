from marshmallow import Schema, fields
from Schemas.schemas import *
from models.logic.GameController import *
from app import db
import json

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    board = db.Column(db.Text, nullable=False)

    def __init__(self, result):
        self.board = json.dumps(
            result
        )

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
            'board': self.board
        }



