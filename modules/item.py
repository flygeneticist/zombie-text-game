
def item_builder(item_attributes):
  return Item(item_attributes)

class Item(object):
  # takes in a tuple of item attributes and returns an item object
  def __init__(self, (name, descrip, carry, weight, breakable, damage)):
    self.name = name
    self.descrip = descrip
    self.carry = carry
    self.weight = weight
    self.breakable = breakable
    self.damage = damage



# test items for unit testing purposes only
test_item_weapon = Item(("Gun","M4 Machine Gun", True, 10, False, 60))
