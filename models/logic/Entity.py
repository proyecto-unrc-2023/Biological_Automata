# class bacterium is a implementation of game's bacterium
from abc import ABC, abstractmethod

class Entity(ABC):

  #Eliminacion
  def delete(self):
    pass

  @staticmethod
  @abstractmethod
  def from_string():
    pass

  @abstractmethod
  def __str__(self):
    pass

  @abstractmethod
  def add_move(self):
    pass