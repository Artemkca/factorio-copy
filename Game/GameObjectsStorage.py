class GameObjectsStorage:
    def __init__(self) -> None:
        self.storage = {}
        self.last_id = 0
        
    def add(self, object):
        self.storage[self.last_id] = object
         
        self.last_id += 1

    def get(self): 
        return self.storage.items()
