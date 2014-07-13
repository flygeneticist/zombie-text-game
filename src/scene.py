from item import Item
# from player import Npc

class Scene(object):
    def __init__(self, name, description, layout, items, npc):
        self.name = name
        self.description = description
        self.layout = layout # directions and which scene they lead to.
        self.items = items
        self.npc = npc

    def open_scene(self):
        return (self.description, self.npc, self.items)