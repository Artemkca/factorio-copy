from ..GameComponent import GameComponent
from ..ComponentController import ComponentController

import pygame


class KeyboardComponent(GameComponent):
    def __init__(self, engine):
        super().__init__()
        
        self.engine = engine
        
        self.controllers = [
            KeyController(self)
        ]
        
    def update(self):
        for controller in self.controllers:
            controller.update()
            
    def draw(self):
        for controller in self.controllers:
            controller.draw()


class KeyController(ComponentController):
    def __init__(self, component):
        super().__init__()
        
        component.a = False
        component.b = False
        component.c = False
        component.d = False
        component.e = False
        component.f = False
        component.g = False
        component.h = False
        component.i = False
        component.j = False
        component.k = False
        component.l = False
        component.m = False
        component.n = False
        component.o = False
        component.p = False
        component.q = False
        component.r = False
        component.s = False
        component.t = False
        component.u = False
        component.v = False
        component.w = False
        component.x = False
        component.y = False
        component.z = False
    
        self.pressed_a = False
        self.pressed_b = False
        self.pressed_c = False
        self.pressed_d = False
        self.pressed_e = False
        self.pressed_f = False
        self.pressed_g = False
        self.pressed_h = False
        self.pressed_i = False
        self.pressed_j = False
        self.pressed_k = False
        self.pressed_l = False
        self.pressed_m = False
        self.pressed_n = False
        self.pressed_o = False
        self.pressed_p = False
        self.pressed_q = False
        self.pressed_r = False
        self.pressed_s = False
        self.pressed_t = False
        self.pressed_u = False
        self.pressed_v = False
        self.pressed_w = False
        self.pressed_x = False
        self.pressed_y = False
        self.pressed_z = False
        
        self.component = component
    
    def update(self):
        for i in range(26):
            value = pygame.key.get_pressed()[pygame.K_a + i]
            key = chr(97 + i)
            pressed = getattr(self.component, key)
            __pressed = getattr(self, "pressed_" + key)
            
            if pressed:
                setattr(self.component, key, False)
            else:
                if not __pressed and value:
                    setattr(self.component, key, True)
                    setattr(self, "pressed_" + key, True)
                if __pressed and not value:
                    setattr(self, "pressed_" + key, False)
                
    def draw(self): ...
