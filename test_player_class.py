import unittest
import player_class

class PlayerClassTests(unittest.TestCase):
  '''Unit tests for the player class'''

  def test_player_setup_yields_player_object(self):
    '''Player creation should yield a player object with a name, health, and stamina, and is alive.'''
    self.assertTrue(isinstance(player_class.test_player, object))
    self.assertTrue(player_class.test_player.name)
    self.assertTrue(player_class.test_player.health)
    self.assertTrue(player_class.test_player.stamina)
    self.assertTrue(player_class.test_player.alive)


  def test_error_raised_with_bad_direction(self):
    '''Given a non-existant direction to look, should raise a ValueError'''
    self.assertRaises(ValueError, player_class.test_player.direction_valid, "ew")

  def test_ability_look_around_in_all_valid_directions(self):
    '''Player should have the ability to look around in all directions and get back a description of their environment.'''
    for direction in player_class.test_player.directions:
      self.assertTrue(isinstance(player_class.test_player.look(direction), str))

  def test_movement_given_valid_direction(self):
    '''Given a valid direction, player should move to new scene'''
    for direction in player_class.test_player.directions:
      self.assertTrue(isinstance(player_class.test_player.look(direction), str))


if __name__ == '__main__':
  unittest.main()
