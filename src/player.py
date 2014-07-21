class Player(object):
    def __init__(self):
        self.name = input("Enter your character's name: ")
        print("\n") # break line to space out first scene's opening text
        self.health = 100
        self.maxhealth = 100
        self.stamina = 100
        self.maxstamina = 100
        self.inv_weight = 0
        self.inventory = {} #setup => {item_name : [obj , quant]}

    def stats_check(self):
        return (str(self.health)+'/'+str(self.maxhealth), str(self.stamina)+'/'+str(self.maxstamina))

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

    def drop_item(self, item, x=1):
        if item.droppable:
            if not (self.check_item_quant(item)):
                return print("That item is not in your inventory to drop.")
            elif self.check_item_quant(item) <= 1:
                self.inventory.pop(item.name, 0)
            else:
                self.inventory[item_name][1] -= x
                inv_weight_update()
            self.inv_weight_update()
            print("You have dropped {0} {1} from your inventory.".format(x, item.name))
            return item
        else:
            return print("You cannot drop special or quest items.")

    def add_item(self, item, x=1):
        if item.carry:
            self.inv_weight_update()
            if (self.inv_weight + item.weight) <= self.maxstamina:
                if not (self.check_item_quant(item)):
                    self.inventory[item.name] = [item, x]
                elif self.check_item_quant(item) >= 0:
                    self.inventory[item_name][1] += x
                else:
                    return print("You cannot add that.")
                return print("You have added {0} {1} to your inventory.".format(x, item.name))
            else:
                return print("You are carry too much to add that. Drop some items first.")
        else: 
            return print("You are not allowed to carry that.")

    def check_inv(self):
        if len(self.inventory) == 0:
            return print("There is naught but some mites of dust in that there bag o yours.")
        else:
            print("Inventory - Item(QTY):")
            for k,v in self.inventory.items():
                print("\t", k, "(", v[1], ")")

    def inv_weight_update(self):
        new_weight = 0
        if len(self.inventory) > 0:
            for k,v in self.inventory.items():
                # adds the item weight times the quantity to the running wight total
                new_weight += (v[0].weight * v[1])
        self.inv_weight = new_weight
        