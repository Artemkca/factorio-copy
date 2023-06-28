from abc import abstractmethod

from .DrawableObject import DrawableObject
from .UpdatableObject import UpdatableObject


class DrawUpdatableObject(DrawableObject, UpdatableObject):
    @abstractmethod
    def draw(self): ...
    
    @abstractmethod
    def update(self): ...
    