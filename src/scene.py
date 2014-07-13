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

    def remove_item(self, item_name):
        if item_name in self.items:
            item = self.items[item_name]
            self.items.pop(item_name, 0)
        else:
            return print("Not a valid item to take.")

    def add_item(self, item_name):
        pass