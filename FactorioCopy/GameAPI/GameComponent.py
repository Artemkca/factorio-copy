from abc import abstractmethod

from .DrawUpdatableObject import DrawUpdatableObject


class GameComponent(DrawUpdatableObject):
    @abstractmethod
    def update(self): ...
    
    @abstractmethod
    def draw(self): ...
