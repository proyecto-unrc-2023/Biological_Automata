from marshmallow import Schema, fields

class CellSchema(Schema):
    #bacterias = fields.List(fields.Str())
    _info_bacteria = fields.Tuple((fields.Str(), fields.Int()), required=True)
    _other = fields.Int()
    _power_other = fields.Int()

class BoardSchema(Schema):
    _rows = fields.Int()
    _columns = fields.Int()
    _board = fields.List(fields.List(fields.Nested(CellSchema)))


class GameSchema(Schema):
    _board = fields.Nested(BoardSchema)
    spawn_bacterium = fields.Tuple((fields.Integer(), fields.Integer()), required=True)
    spawn_other = fields.Tuple((fields.Integer(), fields.Integer()), required=True)
    _game_mode = fields.Str()
    _game_state = fields.Str()
    _game_winner = fields.Str()
    _cant_bacterium = fields.Int()
    _cant_other = fields.Int()
    _max_power_other = fields.Int()
    _moves_for_explotion = fields.Int()
