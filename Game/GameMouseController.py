from .Vector2 import Vector2
from .GameObject import GameObject

import pygame


class GameMouseController(GameObject):
    def __init__(self, engine) -> None:
        super().__init__()
        
        self.engine = engine
        
        self.m1 = False
        self.m2 = False
        self.m3 = False
        
        self.__pressed_m1 = False
        self.__pressed_m2 = False
        self.__pressed_m3 = False
    
    def update(self, _):
        self.position = Vector2(pygame.mouse.get_pos())
        m1, m2, m3 = pygame.mouse.get_pressed()
        
        if self.m1:
            self.m1 = False
        else:
            if not self.__pressed_m1 and m1:
                self.m1 = True
                self.__pressed_m1 = True
            if self.__pressed_m1 and not m1:
                self.__pressed_m1 = False
                
        if self.m2:
            self.m2 = False
        else:
            if not self.__pressed_m2 and m2:
                self.m2 = True
                self.__pressed_m2 = True
            if self.__pressed_m2 and not m2:
                self.__pressed_m2 = False
                
        if self.m3:
            self.m3 = False
        else:
            if not self.__pressed_m3 and m3:
                self.m3 = True
                self.__pressed_m3 = True
            if self.__pressed_m3 and not m3:
                self.__pressed_m3 = False 

    def draw(self, _): ...
