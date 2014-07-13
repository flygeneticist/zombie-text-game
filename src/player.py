from item import Item

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

    def check_item_in_inventory(self, item_name):
        if (item_name in self.inventory):
            return True 
        else:
            return False

    def check_item_quant(self, item_name):
        if (check_item_in_inventory(item_name)):
            return self.inventory[item_name]['quant'] 
        else:
            return False

    def less_x_item(self, item_name, x=1):
        if self.check_item_in_inventory(item_name):
            self.inventory[item_name]['quant'] -= x
            return True
        else:
            return False

    def plus_x_item(self, item_name, x=1):
        if self.check_item_in_inventory(item_name):
            self.inventory[item_name]['quant'] += x
            return True
        else:
            return False

    def drop_inventory_item(self, item):
        if self.check_item_quant(item_name) <= 0: 
            self.inventory.remove(item_name)
            return True
        else:
            return False

    def add_inventory_item(self, item, x=1):
        if self.check_item_quant(item['name']) <= 0: 
            self.inventory[item['name']] = [item, x]
            return True
        else:
            return False