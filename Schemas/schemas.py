from marshmallow import Schema, fields

class CellSchema(Schema):
    bacterias = fields.List(fields.Str())
    _other = fields.Int()

class BoardSchema(Schema):
    _rows = fields.Int()
    _columns = fields.Int()
    _board = fields.List(fields.List(fields.Nested(CellSchema)))


class GameSchema(Schema):
    _board = fields.Nested(BoardSchema)
    spawn_bacterium = fields.Tuple((fields.Integer(), fields.Integer()), required=True)
    spawn_other = fields.Tuple((fields.Integer(), fields.Integer()), required=True)
    _game_mode = fields.Str()
    _cant_bacterium = fields.Int()
    _cant_other = fields.Int()
