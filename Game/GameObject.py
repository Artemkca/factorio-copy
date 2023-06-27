from abc import abstractmethod, ABC


class GameObject(ABC):    
    @abstractmethod
    def update(self, events): ...
    
    @abstractmethod
    def draw(self, screen): ...        
