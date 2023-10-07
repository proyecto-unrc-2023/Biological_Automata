import pytest
from models.logic.Bacterium import Bacterium, BacteriumNormal, BacteriumStrong
from unittest.mock import patch
import random

def test_bacteriumNormal_constructor_validate_moves():
    valid_moves = [0,1,2,3]  # Algunas valores positivos
    for valid_move in valid_moves:
        bacterium = BacteriumNormal(valid_move)
        assert bacterium.moves == valid_move

def test_bacteriumNormal_constructor_negative_moves():
    valid_moves = [-3,-2,-1]  # Algunas valores negativos
    for negative_move in valid_moves:
        bacterium = BacteriumNormal(negative_move)
        assert bacterium.moves == 0

def test_bacteriumNormal_add_move():
    bacterium = BacteriumNormal(0)
    assert bacterium.moves == 0
    bacterium.add_move()
    assert bacterium.moves == 1

def test_bacterium_set_move():
    bacteria = Bacterium(0)
    assert bacteria.moves == 0
    bacteria.moves = 3
    assert bacteria.moves == 3

def test_bacterium_reproducir_normal():
    bacterium = BacteriumNormal(3)
    random.random = lambda: 0.1
    new_bacterium = bacterium.reproducir()
    assert isinstance(new_bacterium, BacteriumNormal) and new_bacterium.moves == 0

def test_bacterium_reproducir_strong():
    bacterium = BacteriumNormal(3)
    random.random = lambda: 0.005
    new_bacterium = bacterium.reproducir()
    assert isinstance(new_bacterium, BacteriumStrong) and new_bacterium.moves == 0

def test_bacteriumNormal_error_reproducible():
    bacterium = BacteriumNormal(2)
    with pytest.raises(ValueError) as e:
        bacterium.reproducir()
    assert str(e.value) == "El número de movimientos no es 3"

def test_bacteriumNormal_isReproducible():
    bacterium = BacteriumNormal(3)
    bool = bacterium.isReproducible()
    assert bool

def test_bacteriumNormal_no_isReproducible():
    bacterium = BacteriumNormal(2)
    bool = bacterium.isReproducible()
    assert not bool

def test_bacteriumNormal_isRecoverable():
    bacterium = BacteriumNormal(0)
    assert not bacterium.isRecoverable()

def test_normal_str():
    bacterium = BacteriumNormal(0)
    assert str(bacterium) == 'b'