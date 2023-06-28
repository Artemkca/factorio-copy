from .GameAPI.GameComponent import GameComponent
from .GameAPI.ComponentController import ComponentController

import pygame


class GameMapComponent(GameComponent):
    def __init__(self, engine):
        super().__init__()
        
        self.engine = engine
        
        self.controllers = [
            DrawController(self)
        ]
    
    def update(self):
        for controller in self.controllers:
            controller.update()
                
    def draw(self):
        for controller in self.controllers:
            controller.draw()


class DrawController(ComponentController):
    def __init__(self, component):
        super().__init__()
        
        self.component = component
    
    def update(self): ...

    def draw(self):
        engine = self.component.engine 
        
        width = engine.width
        height = engine.height
        
        for y in range(height // 64 + 1):
            pygame.draw.line(
                engine.screen,
                (0, 0, 0),
                (0, y * 64),
                (width, y * 64),
                1
            )
            
        for x in range(width // 64 + 1):
            pygame.draw.line(
                engine.screen,
                (0, 0, 0),
                (x * 64, 0),
                (x * 64, height),
                1
            )
