from ..Vector2 import Vector2

from ..GameComponent import GameComponent
from ..ComponentController import ComponentController

import pygame


class MouseComponent(GameComponent):
    def __init__(self, engine):
        super().__init__()
        
        self.engine = engine
        
        self.controllers = [
            MouseLeftClick(self),
            MouseRightClick(self),
            MousePosition(self)
        ]
        
    def update(self):
        for controller in self.controllers:
            controller.update()
            
    def draw(self):
        for controller in self.controllers:
            controller.draw()
        
        
class MouseLeftClick(ComponentController):
    def __init__(self, component):
        super().__init__()
        
        self.clicked = False
        self.pressed = False
        self.__pressed = False
        
        component.left_clicked = False
        component.left_pressed = False
        
        self.component = component
    
    def update(self):
        pressed, _, _ = pygame.mouse.get_pressed()
        
        self.pressed = pressed
        
        self.component.left_pressed = self.pressed
        self.component.left_clicked = self.clicked
        
        if self.clicked:
            self.clicked = False
        else:
            if not self.__pressed and pressed:                
                self.clicked = True
                self.__pressed = True
            if self.__pressed and not pressed:
                self.__pressed = False
                
    def draw(self): ...
                

class MouseRightClick(ComponentController):
    def __init__(self, component):
        super().__init__()
        
        self.clicked = False
        self.pressed = False
        self.__pressed = False
        
        component.right_clicked = False
        component.right_pressed = False
        
        self.component = component
    
    def update(self):
        _, _, pressed = pygame.mouse.get_pressed()
        
        self.pressed = pressed
        
        self.component.right_pressed = self.pressed
        self.component.right_clicked = self.clicked
        
        if self.clicked:
            self.clicked = False
        else:
            if not self.__pressed and pressed:                
                self.clicked = True
                self.__pressed = True
            if self.__pressed and not pressed:
                self.__pressed = False
                
    def draw(self): ...


class MousePosition(ComponentController):
    def __init__(self, component):
        super().__init__()

        component.position = Vector2(0, 0)
        
        self.component = component

    def update(self):
        self.component.position = Vector2(*pygame.mouse.get_pos())
        
    def draw(self): ...
