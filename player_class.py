
class Player():
  '''Common attributes and setup for players (human and NPC)'''

  def __init__(self, name):
    self.name = name
    self.health = 100
    self.stamina = 100
    self.alive = True
    self.inv = {}
    self.directions = ['n','s','e','w']

  def direction_valid(self, direction):
    if direction.lower() in self.directions:
      return direction
    else:
      return 'Direction given is not valid.'

  def look(self, direction):
    if self.direction_valid(direction):
      pass

  def move(self, direction):
    if self.direction_valid(direction):
      pass

  def info(self):
    if self.alive:
      for item in [('Health', self.health), ('Stamina', self.stamina)]:
        yield "{0}: {1}".format(item[0], item[1])
    else:
      print "You are dead! You have no stats."

  def inventory(self):
    if self.inv == {}:
      yield "Your inventory is empty! Go collect some stuff."
    else:
      for item in self.inv:
        yield "{0}: {1}".format(item.name, self.inv[item])

  def pickup(self, item):
    # checks if player has enough stamina to carry the item
    if (self.stamina >= item.weight and item.carry):
      if item in self.inv:
        self.inv[item] += 1 # already in inventory
      else:
        self.inv[item] = 1 #
      return "You have added the {} to your inventory.".format(item.name)
    else:
      return "You are out of stamina and cannot add any more items."

  def examine(self, item):
    pass

  def attack(self, weapon):
    pass


# Empty Player object for unit testing use.
test_player = Player("Rick")
