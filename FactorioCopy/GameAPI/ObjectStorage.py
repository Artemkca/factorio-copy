from .DrawableObject import DrawableObject
from .UpdatableObject import UpdatableObject
from .DrawUpdatableObject import DrawUpdatableObject


class ObjectStorage:
    def __init__(self):
        self.storage = []
    
    def add_object(self, object):
        if isinstance(object, DrawUpdatableObject):
            object_type = "draw_updatable"
        
        elif isinstance(object, DrawableObject):
            object_type = "drawable"
            
        elif isinstance(object, UpdatableObject):
            object_type = "updatable"
            
        self.storage.append((
            object_type,
            object
        ))

    def get_draw_updatable(self):
        return [object[1] for object in self.storage]

    def get_drawable(self):
        return [object[1] for object in self.storage if object[0] in ("drawable", "draw_updatable")]
    
    def get_updatable(self):
        return [object[1] for object in self.storage if object[0] in ("updatable", "draw_updatable")]
