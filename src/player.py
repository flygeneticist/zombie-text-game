class Player(object):
    def __init__(self):
        self.name = input("Enter your character's name: ")
        self.health = 100
        self.maxhealth = 100
        self.stamina = 100
        self.maxstamina = 100
        self.inventory = {} #setup => {item_name : [obj , quant]}

    def check_if_dead(self):
        if health > 0:
            return True
        else:
            return False

    def check_item_in_inventory(self, item):
        try:
            self.inventory[item.name]
        except KeyError:
            return False
        else:
            return True

    def check_item_quant(self, item):
        if self.check_item_in_inventory(item):
            return self.inventory[item.name][1]
        else:
            return False

    def drop_item(self, item):
        if not (self.check_item_quant(item)):
            return print("That item is not in your inventory to drop.")
        elif self.check_item_quant(item) <= 1:
            self.inventory.pop(item.name, 0)
        else:
            self.inventory[item_name][1] -= x
        return print("You have added {0} {1} to your inventory.").format(x, item.name)

    def add_item(self, item, x=1):
        if not (self.check_item_quant(item)):
            self.inventory[item.name] = [item, x]
        elif self.check_item_quant(item) >= 0:
            self.inventory[item_name][1] += x
        else:
            return print("You cannot add that.")
        return print("You have added {0} {1} to your inventory.").format(x, item.name)