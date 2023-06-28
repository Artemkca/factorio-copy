from abc import abstractmethod

from .DrawUpdatableObject import DrawUpdatableObject


class ComponentController(DrawUpdatableObject):
    @abstractmethod
    def update(self): ...
    
    @abstractmethod
    def draw(self): ...
