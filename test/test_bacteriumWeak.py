import pytest
from models.logic.Bacterium import Bacterium, BacteriumWeak

def test_weakBacterium_constructor_validate_moves():
    valid_moves = [0,1,2,3]  # Algunas valores positivos
    for valid_move in valid_moves:
        bacterium = BacteriumWeak(valid_move)
        assert bacterium.moves == valid_move

def test_weakBacterium_constructor_negative_moves():
    valid_moves = [-3,-2,-1]  # Algunas valores negativos
    for negative_move in valid_moves:
        bacterium = BacteriumWeak(negative_move)
        assert bacterium.moves == 0

def test_weakBacterium_add_move():
    bacterium = BacteriumWeak(0)
    assert bacterium.moves == 0
    bacterium.add_move()
    assert bacterium.moves == 1

def test_bacterium_set_increment():
    bacteria = BacteriumWeak(0)
    assert bacteria.moves == 0
    bacteria.moves = 3
    assert bacteria.moves == 3

def test_weakBacterium_not_reproducible():
    bacterium = BacteriumWeak(3)
    assert bacterium.isReproducible() == False

def test_weakBacterium_return_state():
    bacterium = BacteriumWeak(6)
    assert bacterium.isRecoverable() == True

def test_weakBacterium_not_return_state():
    bacterium = BacteriumWeak(3)
    assert bacterium.isRecoverable() == False

def test_weakBacterium_str():
    bacterium = BacteriumWeak(0)
    assert str(bacterium) == 'd'

def test_weakBaterium_from_string():
    cell_str = str(BacteriumWeak(0))
    bacterium = Bacterium.from_string(cell_str)
    assert isinstance(bacterium, BacteriumWeak)