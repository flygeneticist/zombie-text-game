
class Player():
  '''Common attributes and setup for players (human and NPC)'''

  def __init__(self, name):
    self.name = name
    self.health = 100
    self.stamina = 100
    self.alive = True
    self.directions = ['n','s','e','w']

  def direction_valid(self, direction):
    if direction.lower() in self.directions:
      return direction
    else:
      raise ValueError('Direction given is not valid.')

  def look(self, direction):
    if self.direction_valid(direction):
      pass

  def move(self, direction):
    if self.direction_valid(direction):
      pass

test_player = Player("Rick")
