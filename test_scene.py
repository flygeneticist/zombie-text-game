import unittest
import scene

class SceneTests(unittest.TestCase):

  def test_death(self):
    '''Death scene should output final message to player and offer replay.'''
    self.assertTrue(scene.Death)

if __name__ == '__main__':
  unittest.main()

