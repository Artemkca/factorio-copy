from .GameMap import GameMap
from .Application import Application
from .GameObjectsStorage import GameObjectsStorage


class GameEngine(Application):
    def init(self):
        self.map = GameMap()
        self.objects = GameObjectsStorage()
    
    def update(self):
        for id, object in self.objects.get():
            ...
    
    def draw(self): ...
