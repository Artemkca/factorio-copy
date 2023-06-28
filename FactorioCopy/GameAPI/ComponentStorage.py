class ComponentStorage:
    def __init__(self) -> None:
        self.storage = {}
    
    def add_component(self, component_name, component):
        self.storage[component_name] = component

    def get_component(self, component_name):
        return self.storage.get(component_name)
