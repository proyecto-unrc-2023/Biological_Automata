
import pytest
from models.logic.Bacterium import *


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
    new_bacterium = bacterium.isReproducible()
    assert bacterium.moves == 3
    assert new_bacterium != None

def test_normal_error_reproducible():
    bacterium = BacteriumNormal(2)
    with pytest.raises(ValueError):
        res = bacterium.reproducir()


def test_normal_str():
    bacterium = BacteriumNormal(0)
    assert str(bacterium) == 'b'

def test_strong_str():
    bacterium = BacteriumStrong(0)
    assert str(bacterium) == 'f'
