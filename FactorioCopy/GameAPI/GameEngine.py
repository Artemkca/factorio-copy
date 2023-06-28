from .Application import Application

from .ObjectStorage import ObjectStorage
from .ComponentStorage import ComponentStorage

from .BuiltinComponents import MouseComponent, EventsComponent, KeyboardComponent


class GameEngine(Application):
    def __init__(self, width, height, fps):
        super().__init__(width, height, fps)
        
        self.objects = ObjectStorage()
        self.components = ComponentStorage()
        
        self.add_component("Events", EventsComponent(self))
        self.add_component("Mouse", MouseComponent(self))
        self.add_component("Keyboard", KeyboardComponent(self))

    def add_object(self, object):
        self.objects.add_object(object)

    def add_component(self, component_name, component):
        self.add_object(component)
        
        self.components.add_component(component_name, component)

    def get_component(self, component_name):
        return self.components.get_component(component_name)

    def update(self):
        for updatable_object in self.objects.get_updatable():
            updatable_object.update()

    def draw(self):
        for drawable_object in self.objects.get_drawable():
            drawable_object.draw()
