import pytest
from models.logic.Bacterium import BacteriumStrong


def test_strong_reproducible():
    bacterium = BacteriumStrong(3)
    ente = bacterium.reproducir()
    assert isinstance(ente, BacteriumStrong) == True

def test_strong_reproducible_error():
    bacterium = BacteriumStrong(2)
    with pytest.raises(ValueError):
        res = bacterium.reproducir()


def test_strong_str():
    bacterium = BacteriumStrong(0)
    assert str(bacterium) == 'f'
