from abc import abstractmethod, ABC


class GameObject(ABC):
    def __init__(self, position) -> None:
        super().__init__()
        
        self.position = position
    
    @abstractmethod
    def update(self): ...
    
    @abstractmethod
    def draw(self): ...
