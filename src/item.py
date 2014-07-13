class Item(object):
    # takes in a tuple of item attributes and returns an item object
    # data should => (name(str), descrip(str), carry(bit), breakable(int), health(int), weight(int), droppable(bit), equipable(bit)) 
    def __init__(self, data):
        self.name, self.descrip, self.carry, self.breakable, self.health, self.weight, self.droppable, self.equipable = data

    def check_if_broken(self):
        if self.health > 0:
            return False
        else:
            return True

