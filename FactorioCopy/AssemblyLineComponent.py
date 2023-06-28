from .GameAPI.Vector2 import Vector2
from .GameAPI.DrawUpdatableObject import DrawUpdatableObject

from .GameAPI.GameComponent import GameComponent
from .GameAPI.ComponentController import ComponentController

import pygame


class AssemblyLine(DrawUpdatableObject):
    def __init__(self, engine, position):
        super().__init__()
        
        self.engine = engine
        
        self.state = 0
        
        self.assembly_line_texture1 = pygame.image.load("textures\\AssemblyLine1.png").convert_alpha()
        self.assembly_line_texture2 = pygame.image.load("textures\\AssemblyLine2.png").convert_alpha()
        self.assembly_line_texture3 = pygame.image.load("textures\\AssemblyLine3.png").convert_alpha()
        self.assembly_line_texture4 = pygame.image.load("textures\\AssemblyLine4.png").convert_alpha()
        self.assembly_line_texture5 = pygame.image.load("textures\\AssemblyLine5.png").convert_alpha()
        self.assembly_line_texture6 = pygame.image.load("textures\\AssemblyLine6.png").convert_alpha()
        
        self.position = position

    def update(self): ...
    
    def draw(self):
        if self.state == 0:
            assembly_line_texture = self.assembly_line_texture1
        if self.state == 1:
            assembly_line_texture = self.assembly_line_texture2
        if self.state == 2:
            assembly_line_texture = self.assembly_line_texture3
        if self.state == 3:
            assembly_line_texture = self.assembly_line_texture4
        if self.state == 4:
            assembly_line_texture = self.assembly_line_texture5
        if self.state == 5:
            assembly_line_texture = self.assembly_line_texture6
        
        self.engine.screen.blit(
            assembly_line_texture,
            self.position.get()
        )


class AssemblyLinePhantom(AssemblyLine):
    def draw(self):
        if self.state == 0:
            assembly_line_texture = self.assembly_line_texture1
        if self.state == 1:
            assembly_line_texture = self.assembly_line_texture2
        if self.state == 2:
            assembly_line_texture = self.assembly_line_texture3
        if self.state == 3:
            assembly_line_texture = self.assembly_line_texture4
        if self.state == 4:
            assembly_line_texture = self.assembly_line_texture5
        if self.state == 5:
            assembly_line_texture = self.assembly_line_texture6
        
        self.engine.screen.blit(
            assembly_line_texture,
            self.position.get()
        )
        
        del self


class AssemblyLineComponent(GameComponent):
    def __init__(self, engine):
        super().__init__()
        
        self.engine = engine
        
        self.controllers = [
            AssemblyLineCreator(self)
        ]
        
    def update(self):
        for controller in self.controllers:
            controller.update()
            
    def draw(self):
        for controller in self.controllers:
            controller.draw()


class AssemblyLineCreator(ComponentController):
    def __init__(self, component):
        super().__init__()
        
        self.state = 0
        self.r_pressed = False
        
        self.component = component

    def update(self):
        mouse = self.component.engine.get_component("Mouse")
        
        if self.component.engine.get_component("Keyboard").r:
            self.state += 1
        
        if mouse.left_clicked:
            x, y = mouse.position.get()
            
            assembly_line = AssemblyLine(
                self.component.engine,
                Vector2(x // 64 * 64, y // 64 * 64)
            )
            
            assembly_line.state = self.state % 6
            
            self.component.engine.add_object(assembly_line)
        
    def draw(self):
        mouse = self.component.engine.get_component("Mouse")
        
        x, y = mouse.position.get()
            
        assembly_line_phantom = AssemblyLinePhantom(
            self.component.engine,
            Vector2(x // 64 * 64, y // 64 * 64)
        )
        
        assembly_line_phantom.state = self.state % 6
        
        assembly_line_phantom.draw()
