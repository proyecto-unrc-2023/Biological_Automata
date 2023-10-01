from marshmallow import Schema, fields
from models.logic.GameController import GameController

class BacteriophageSchema(Schema):
    infection = fields.Int()

class BacteriumSchema(Schema):
    moves = fields.Int()

class CellSchema(Schema):
    _bacteria = fields.Nested(BacteriumSchema, many=True)
    _antibiotics = fields.Int()
    _bacteriophages = fields.Nested(BacteriophageSchema, many=True)
    is_spawn = fields.Bool()

class BoardSchema(Schema):
    _rows = fields.Int()
    _columns = fields.Int()
    _board = fields.Nested(CellSchema, many=True, many_nested=True)

class GameSchema(Schema):
    board = fields.Nested(BoardSchema)

