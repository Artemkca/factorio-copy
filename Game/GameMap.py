from .GameObject import GameObject

import pygame

class GameMap(GameObject):
    def __init__(self, engine) -> None:
         super().__init__()
         
         self.engine = engine
         
         self.width = engine.width
         self.height = engine.height
    
    def update(self, _): ...
    
    def draw(self, screen):
        for y in range(self.height // 64 + 1):
            pygame.draw.line(
                screen,
                (0, 0, 0),
                (0, y * 64),
                (self.width, y * 64),
                1
            )
            
        for x in range(self.width // 64 + 1):
            pygame.draw.line(
                screen,
                (0, 0, 0),
                (x * 64, 0),
                (x * 64, self.height),
                1
            )
