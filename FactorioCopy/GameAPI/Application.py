from abc import abstractmethod

from .GameObject import GameObject

import pygame


class Application(GameObject):
    def __init__(self, width, height, fps) -> None:
        self.fps = fps
        self.width = width
        self.height = height
        
        pygame.init()
        
        self.screen = pygame.display.set_mode((
            self.width, 
            self.height
        ))
        
        self.clock = pygame.time.Clock()
    
    @abstractmethod
    def update(self): ...
    
    @abstractmethod
    def draw(self): ...
    
    def _draw(self):
        self.screen.fill((255, 255, 255))
        
        self.draw()
        
        pygame.display.update()
    
    def run(self) -> None:
        while 1:
            self.update()
            self._draw()

            self.clock.tick(self.fps)
