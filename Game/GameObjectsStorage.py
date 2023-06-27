from collections import defaultdict


class GameObjectsStorage:
    def __init__(self) -> None:
        self.storage = defaultdict(list)
        
    def add(self, object, name=""):
        self.storage[name].append(object)

    def get(self, name=""):
        if name:
            return self.storage[name]
        else:
            return sum(map(lambda x: x[1], self.storage.items()), [])
