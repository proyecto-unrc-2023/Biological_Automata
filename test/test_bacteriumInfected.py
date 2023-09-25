import pytest
from models.logic.Bacterium import *

def test_bacterium_move_increment():
    bacteria = BacteriumInfected(0)  
    bacteria.add_move()
    assert bacteria.moves == 1

def test_bacterium_set_increment():
    bacteria = BacteriumInfected(0)
    bacteria.moves = 3
    assert bacteria.moves == 3

def test_lithic_state():
    bacterium = BacteriumInfected(4)
    result = bacterium.lithic_State()
    assert result == True
    bacterium.exploid()
    with pytest.raises(AssertionError):
        assert bacterium == None

def test_infectedBacterium_not_reproducible():
    bacterium = BacteriumInfected(3)
    assert bacterium.isReproducible() == False

def test_infectedBacterium_str():
    bacterium = BacteriumInfected(0)
    assert str(bacterium) == 'i'

def test_infectedBaterium_from_string():
    cell_str = str(BacteriumInfected(0))
    bacterium = Bacterium.from_string(cell_str)
    assert isinstance(bacterium, BacteriumInfected)
