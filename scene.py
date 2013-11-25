class Scene(object):

  def __init__(self, name):
    self.name = name



class Death(Scene):

  def __init__(self, player):
    if player.alive:
      return False
    else:
      return "You have died. How unfortunate."

