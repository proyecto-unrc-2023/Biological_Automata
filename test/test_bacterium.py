import pytest
from models.logic.Bacterium import *
from unittest.mock import patch

def test_bacterium_constructor_validate_moves():
    valid_moves = [0,1,2,3]  # Algunas valores positivos
    for valid_move in valid_moves:
        bacterium = Bacterium(valid_move)
        assert bacterium.moves == valid_move

def test_bacterium_constructor_negative_moves():
    valid_moves = [-3,-2,-1]  # Algunas valores negativos
    for negative_move in valid_moves:
        bacterium = Bacterium(negative_move)
        assert bacterium.moves == 0

def test_bacterium_add_move():
    bacterium = Bacterium(0)
    bacterium.add_move()
    assert bacterium.moves == 1

def test_bacterium_isReproducible():
    bacterium = Bacterium(1)
    value = bacterium.isReproducible()
    assert bacterium.moves == 1 and value == None

def test_bacterium_isRecoverable():
    bacterium = Bacterium(1)
    value = bacterium.isRecoverable()
    assert bacterium.moves == 1 and value == None

def test_bacterium_set_increment():
    bacterium = Bacterium(0)
    assert bacterium.moves == 0
    bacterium.moves = 3
    assert bacterium.moves == 3

def test_bacteriumNormal_from_string():
    cell_str = str(BacteriumNormal(0))
    bacterium = Bacterium.from_string(cell_str)
    assert isinstance(bacterium, BacteriumNormal)

def test_bacteriumStrong_from_string():
    cell_str = str(BacteriumStrong(0))
    bacterium = Bacterium.from_string(cell_str)
    assert isinstance(bacterium, BacteriumStrong)

def test_bacteriumInfected_from_string():
    cell_str = str(BacteriumInfected(0))
    bacterium = Bacterium.from_string(cell_str)
    assert isinstance(bacterium, BacteriumInfected)

def test_bacteriumWeak_from_string():
    cell_str = str(BacteriumWeak(0))
    bacterium = Bacterium.from_string(cell_str)
    assert isinstance(bacterium, BacteriumWeak)

def test_bacterium_from_string_invalid():
    invalid_strings = ['c', 'g', 'e', 'debil']  # Algunas cadenas no válidas
    for invalid_str in invalid_strings:
        with pytest.raises(ValueError) as e:
            Bacterium.from_string(invalid_str)
        assert str(e.value) == f'Invalid Bacterium string: {invalid_str}'