import pytest
from models.logic.Bacterium import Bacterium, BacteriumNormal, BacteriumStrong
from unittest.mock import patch
import random


def test_bacteriumNormal_error_reproducible():
    bacterium = BacteriumNormal(2)
    with pytest.raises(ValueError) as e:
        bacterium.reproducir()
    assert str(e.value) == "La bacteria no está en condiciones de reproducirse!"

def test_bacterium_replicate_with_parameter_to_normal():
    bacterium = BacteriumNormal(3)
    new_bacterium = bacterium.replicate_with_parameter(0.2)
    assert isinstance(new_bacterium, BacteriumNormal) and new_bacterium.moves == 0

def test_bacterium_replicate_with_parameter_to_strong():
    bacterium = BacteriumNormal(3)
    new_bacterium = bacterium.replicate_with_parameter(0.05)
    assert isinstance(new_bacterium, BacteriumStrong) and new_bacterium.moves == 0

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