import pytest
from models.logic.Antibiotic import Antibiotic


def test_str_antibiotic():
  antibiotic = Antibiotic()
  assert str(antibiotic) == 'a'


def test_from_str_antibiotic():
  ente = Antibiotic.from_string('a')
  assert isinstance(ente, Antibiotic) == True

def test_from_str_antibiotic_error():
  with pytest.raises(ValueError):
    antibiotic2 = Antibiotic.from_string('b')
