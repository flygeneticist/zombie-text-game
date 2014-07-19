class Item(object):
    # takes in a tuple of item attributes and returns an item object
    # data should => (name(str), descrip(str), carry(bit), breakable(int), health(int), weight(int), droppable(bit), equipable(bit), attack_dmg(int)) 
    def __init__(self, data):
        self.name, self.description, self.carry, self.breakable, self.health, self.weight, self.droppable, self.equipable, self.attack_dmg = data

    def check_if_broken(self):
        if self.health > 0:
            return False
        else:
            return True

    def examine_info(self):
        return (self.description, self.weight+"lbs", self.attack_dmg+"pts")