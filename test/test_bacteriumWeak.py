from models.logic.Bacterium import Bacterium, BacteriumWeak


def test_weakBacterium_not_reproducible():
    bacterium = BacteriumWeak(3)
    assert not bacterium.isReproducible()


def test_weakBacterium_return_state():
    bacterium = BacteriumWeak(6)
    assert bacterium.isRecoverable()


def test_weakBacterium_not_return_state():
    bacterium = BacteriumWeak(3)
    assert not bacterium.isRecoverable()


def test_weakBacterium_str():
    bacterium = BacteriumWeak(0)
    assert str(bacterium) == 'd'


def test_weakBaterium_from_string():
    cell_str = str(BacteriumWeak(0))
    bacterium = Bacterium.from_string(cell_str)
    assert isinstance(bacterium, BacteriumWeak)
