class Item(object):
    # takes in a tuple of item attributes and returns an item object
    # data should => (name, descrip, carry(bool), breakable(bool), health(int), weight(int)) 
    def __init__(self, data):
        self.name, self.descrip, self.carry, self.breakable, self.health, self.weight = data

    def check_if_broken(self):
        if self.health > 0:
            return False
        else:
            return True