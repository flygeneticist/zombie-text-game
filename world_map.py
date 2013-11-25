class Map(object):

  scenes = {}

  def __init__(self, start_scene):
    if start_scene != 'your_hospital_room':
      raise ValueError('Game must start with the scene in your hospital room.')
    else:
      pass
