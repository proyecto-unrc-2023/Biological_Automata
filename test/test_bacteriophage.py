import pytest
from models.logic.Bacteriophage import *


def test_bacteriophage_set_infection():
    virus = Bacteriophage(0)
    virus.infection = 4
    assert virus.infection == 4

def test_bacteriophage_add_move():
    infection_level = 4
    virus = Bacteriophage(infection_level)
    virus.add_move()
    assert virus.infection == infection_level - 1

def test_bacteriophage_moment_death_then():
    virus = Bacteriophage(0)
    assert virus.moment_death()

def test_bacteriophage_moment_death_else():
    virus = Bacteriophage(1)
    assert not virus.moment_death()

def test_bacteriophage_degradation():
    virus = Bacteriophage(0)
    assert virus.degradation() == None

def test_bacteriophage_from_string():
    virus = Bacteriophage.from_string('v')
    assert isinstance(virus, Bacteriophage)

def test_bacteriophage_str():
    virus = Bacteriophage(4)
    assert str(virus) == 'v'

def test_bacteriophage_from_string_invalid():
    with pytest.raises(ValueError) as e:
        Bacteriophage.from_string('virus')
    assert str(e.value) == "Invalid Bacteriofago string: virus"