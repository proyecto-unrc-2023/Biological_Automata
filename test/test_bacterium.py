import pytest
from models.logic.Bacterium import Bacterium, BacteriumNormal, BacteriumStrong
from unittest.mock import patch
import random

def test_bacterium_move_increment():
    bacteria = Bacterium(0)  # Puedes cambiar a cualquier subclase
    bacteria.add_move()
    assert bacteria.moves == 1

def test_bacterium_set_increment():
    bacteria = Bacterium(0)  # Puedes cambiar a cualquier subclase
    bacteria.moves = 3
    assert bacteria.moves == 3

def test_normal_reproducible():
    bacterium = BacteriumNormal(3)
    assert bacterium.moves == 3
    ente = bacterium.reproducir()
    assert bacterium.moves == 0
    assert isinstance(bacterium, BacteriumNormal) == True

def test_normal_error_reproducible():
    bacterium = BacteriumNormal(2)
    with pytest.raises(ValueError):
        res = bacterium.reproducir()

def test_normal_str():
    bacterium = BacteriumNormal(0)
    assert str(bacterium) == 'b'
