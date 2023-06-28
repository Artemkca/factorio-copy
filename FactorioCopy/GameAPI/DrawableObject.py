from abc import abstractmethod, ABC


class DrawableObject(ABC):
    @abstractmethod
    def draw(self): ...
