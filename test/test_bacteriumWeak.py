import pytest
from models.logic.Bacterium import Bacterium, BacteriumWeak

@pytest.fixture
def bacterium_weak():
    return BacteriumWeak(0)

def test_weakBacterium_not_reproducible(bacterium_weak):
    moves_for_reproduction = bacterium_weak.moves_for_reproduction
    bacterium = BacteriumWeak(moves_for_reproduction)
    assert bacterium.isReproducible() == False

def test_weakBacterium_return_state(bacterium_weak):
    moves_for_recovery = bacterium_weak.moves_for_recovery
    bacterium = BacteriumWeak(moves_for_recovery)
    assert bacterium.isRecoverable() == True

def test_weakBacterium_not_return_state(bacterium_weak):
    moves_for_recovery = bacterium_weak.moves_for_recovery
    bacterium = BacteriumWeak(moves_for_recovery - 1)
    assert bacterium.isRecoverable() == False

def test_weakBacterium_str():
    bacterium = BacteriumWeak(0)
    assert str(bacterium) == 'd'

def test_weakBaterium_from_string():
    cell_str = str(BacteriumWeak(0))
    bacterium = Bacterium.from_string(cell_str)
    assert isinstance(bacterium, BacteriumWeak)