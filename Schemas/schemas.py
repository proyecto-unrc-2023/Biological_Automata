from marshmallow import Schema, fields

class BacteriophageSchema(Schema):
    infection = fields.Int()

class BacteriumSchema(Schema):
    moves = fields.Int()

class CellSchema(Schema):
    _bacteria = fields.Nested(BacteriumSchema, many=True)
    _antibiotics = fields.Int()
    _bacteriophages = fields.Nested(BacteriophageSchema, many=True)
    _spawn_bacterium = fields.Bool()
    _spawn_other = fields.Bool()


class BoardSchema(Schema):
    _rows = fields.Int()
    _columns = fields.Int()
    _board = fields.List(fields.List(fields.Nested(CellSchema)))


class GameSchema(Schema):
    _board = fields.Nested(BoardSchema)

