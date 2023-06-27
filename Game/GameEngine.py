from .GameMap import GameMap
from .Application import Application
from .GameMainConroller import GameMainConroller
from .GameObjectsStorage import GameObjectsStorage


class GameEngine(Application):
    def __init__(self, width=600, height=400, fps=60):
        super().__init__(width, height, fps)
        
        self.objects = GameObjectsStorage()
        
        self.objects.add(GameMap(self), "Map")
        self.objects.add(GameMainConroller(self), "Controller")

    def update(self, events):
        for object in self.objects.get():
            object.update(events)

    def draw(self):
        for object in self.objects.get():
            object.draw(self.screen)
