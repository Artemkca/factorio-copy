from ..GameComponent import GameComponent
from ..ComponentController import ComponentController

import pygame


class EventsComponent(GameComponent):
    def __init__(self, engine):
        super().__init__()
        
        self.engine = engine
        
        self.controllers = [
            ExitController(self)
        ]

    def update(self):
        for controller in self.controllers:
            controller.update()
            
    def draw(self):
        for controller in self.controllers:
            controller.draw()


class ExitController(ComponentController):
    def __init__(self, component):
        super().__init__()
        
        self.component = component
    
    def update(self):
        if pygame.event.get(pygame.QUIT):
            pygame.quit()
            
            raise SystemExit()
        
    def draw(self): ...
