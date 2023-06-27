from abc import abstractmethod, ABC

import pygame


class Application(ABC):
    def __init__(self, width=600, height=400, fps=60) -> None:        
        super().__init__()
        
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
    def init(self): ...
        
    @abstractmethod
    def update(self): ...
    
    @abstractmethod
    def draw(self): ...
    
    def run(self) -> None:        
        while 1:
            if pygame.QUIT in map(lambda x: x.type, pygame.event.get()):
                pygame.quit()
                exit()
            
            self.update()
            self.draw()

            self.clock.tick(self.fps)
