from .GameAPI.GameEngine import GameEngine

from .GameMapComponent import GameMapComponent
from .AssemblyLineComponent import AssemblyLineComponent


class Engine(GameEngine):
    def __init__(self):
        super().__init__(
            width=1000,
            height=500,
            fps=60
        )
        
        self.add_component("GameMap", GameMapComponent(self))
        self.add_component("AssemblyLine", AssemblyLineComponent(self))
