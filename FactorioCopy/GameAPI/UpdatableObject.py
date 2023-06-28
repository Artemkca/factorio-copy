from abc import abstractmethod, ABC


class UpdatableObject(ABC):
    @abstractmethod
    def update(self): ...
