from src.item import Item
# from player import Npc

class Scene(object):
    def __init__(self, name, description, layout, items, npc):
        self.name = name
        self.description = description
        self.layout = layout # directions and which scene they lead to.
        self.items = items
        self.npc = npc

    def remove_item(self, item_name):
        if item_name in self.items:
            item = self.items[item_name]
            self.items.pop(item_name, 0)
        else:
            return print("Not a valid item to take.")

    def add_item(self, item):
        self.items[item.name] = item

    def list_items(self):
        if self.items == {}:
            return print("There are no items here.")
        else:
            print("The following items are here:")
            for k,v in self.items.items(): 
                print(self.items[k].name)

    def examine_item(self, item_name):
        try:
            item = self.items[item_name]
        except KeyError:
            return print("Not a valid item.")
        else:
            examined_item = item.examine_info()
            return print("{0}\nWeight: {1}\nAttack Damage: {2}".format(examined_item[0], examined_item[1], examined_item[2]))