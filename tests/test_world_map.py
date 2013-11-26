import unittest
import world_map

class MapTests(unittest.TestCase):

  def test_map_returns_map_opject_containing_scenes(self):
    '''Instantiatng a Map object should return an object with scenes.'''
    self.assertTrue(isinstance(world_map.Map, object))

  def test_Map_class_should_have_a_list_of_scenes(self):
    '''Map class should have a dictionary of possible scenes inside it.'''
    self.assertTrue(isinstance(world_map.Map.scenes, dict))

  def test_map_does_not_start_with_opening_scene_in_hospital_room(self):
    '''Map initilization should take the opening scene in the hospital and none other.'''
    self.assertRaises(ValueError, world_map.Map, 'different_scene')

if __name__ == '__main__':
  unittest.main()
