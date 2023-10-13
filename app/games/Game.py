from marshmallow import Schema, fields
from app import db
import json

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    level = db.Column(db.Integer)
    board = db.Column(db.Text)

    def __init__(self, name, level='Low'):
        self.name = name
        self.level = level
        self.board = json.dumps(
            "[ [[''], [''], [''], ['']], [[''], [''], [''], ['']]]"
        )

    def __repr__(self):
        return self.name

    def json(self):
        return {
            'name': self.name,
            'id': self.id,
            'level': self.level,
            'board': self.board
        }



