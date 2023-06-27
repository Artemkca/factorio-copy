from .GameObject import GameObject

from .GameMouseController import GameMouseController
# from .GameKeyboardController import GameKeyboardController

import pygame


class GameMainConroller(GameObject):
    def __init__(self, engine) -> None:
        super().__init__()
        
        self.engine = engine
        
        self.mouse = GameMouseController(engine)
        
        self.base_controllers = (
            self.mouse,
            # GameKeyboardController()
        )
    
    def update(self, events):
        for controller in self.base_controllers:
            controller.update(events)
        
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
        if self.mouse.m1:
            print(1)

    def draw(self, screen): ...
