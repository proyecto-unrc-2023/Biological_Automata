import pytest
from models.logic.Bacterium import *

# from unittest.mock import patch
# import random

@pytest.fixture
def bacterium_normal():
    return BacteriumNormal(0)

@pytest.fixture
def always_zero():

    return lambda: 0.0

@pytest.fixture
def always_one():
    return lambda: 1.0

#def zero():
#    return 0.0
#class TestClass():
#
#    def __init__(self, random_gen=random.random):
#        self.random_generator = random_gen
#
#    def new_value(self):
#        return self.random_generator()
#
#
#def test_1():
#    tc = TestClass(zero)
#    assert 0.0 == tc.new_value()
#
#
#always_zero = lambda: 0.0
#always_one = lambda: 1.0
#
#def test_2():
#    tc = TestClass(always_zero)
#    assert 0.0 == tc.new_value()
#
#
#def test_3():
#    tc = TestClass(always_one)
#    assert 1.0 == tc.new_value()
    #bact = BacteriumNormal(8, RandomMock(1))
    #bact2 = BacteriumNormal(8)

def test_bacteriumNormal_error_reproducible(bacterium_normal):
    moves_for_reproduction = bacterium_normal.moves_for_reproduction
    bacterium = BacteriumNormal(moves_for_reproduction-1)
    with pytest.raises(ValueError) as e:
        bacterium_normal.reproduce()
    assert str(e.value) == "La bacteria no está en condiciones de reproducirse!"

def test_bacterium_replicate_with_parameter_greater_to_mutation_probability(bacterium_normal, always_zero):
    moves_for_reproduction = bacterium_normal.moves_for_reproduction
    bacterium = BacteriumNormal(moves = moves_for_reproduction, random_gen=always_zero)
    new_bacterium = bacterium.reproduce()
    assert isinstance(new_bacterium, BacteriumStrong) and new_bacterium.moves == 0

def test_bacterium_replicate_with_parameter_1_probability_to_mute(bacterium_normal, always_one):
    moves_for_reproduction = bacterium_normal.moves_for_reproduction
    bacterium = BacteriumNormal(moves_for_reproduction, random_gen=always_one)
    new_bacterium = bacterium.reproduce()
    assert isinstance(new_bacterium, BacteriumNormal) and new_bacterium.moves == 0

def test_bacteriumNormal_isReproducible(bacterium_normal):
    moves_for_reproduction = bacterium_normal.moves_for_reproduction
    bacterium = BacteriumNormal(moves_for_reproduction)
    assert bacterium.isReproducible()


def test_bacteriumNormal_no_isReproducible(bacterium_normal):
    moves_for_reproduction = bacterium_normal.moves_for_reproduction
    bacterium = BacteriumNormal(moves_for_reproduction-2)
    assert not bacterium.isReproducible()


def test_bacteriumNormal_isRecoverable():
    bacterium = BacteriumNormal(0)
    assert not bacterium.isRecoverable()


def test_normal_str():
    bacterium = BacteriumNormal(0)
    assert str(bacterium) == 'b'
