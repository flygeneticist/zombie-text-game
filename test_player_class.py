import unittest
import player_class
import item

class PlayerClassTests(unittest.TestCase):
  '''Unit tests for the player class'''

  def test_player_setup_yields_player_object(self):
    '''Player creation should yield a player object with a name, health, and stamina, an empty inventory, and is alive.'''
    self.assertTrue(isinstance(player_class.test_player, object))
    self.assertTrue(player_class.test_player.name)
    self.assertTrue(player_class.test_player.health)
    self.assertTrue(player_class.test_player.stamina)
    self.assertTrue(player_class.test_player.alive)
    self.assertTrue(player_class.test_player.inv == {})

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

  def test_inventory_is_empty_return_empty_message(self):
    '''Inventory check should return message if empty'''
    result = []
    for output in player_class.test_player.inventory():
        result.append(output)
    self.assertEqual(result, ["Your inventory is empty! Go collect some stuff."])

  def test_success_when_add_item_to_inventory_with_enough_stamina(self):
    '''Player should get a success message if have enough (+1) stamina when adding an item.'''
    self.assertEqual(player_class.Player("Test").pickup(item.test_item_weapon), "You have added the Gun to your inventory.")

  def test_return_inventory_contents_when_valid(self):
    '''Player should get printout of inventory items and quantity when not empty.'''
    person = player_class.Player("Test Person")
    person.pickup(item.test_item_weapon)
    result = []
    for output in person.inventory():
      result.append(output)
    self.assertEqual(result,["Gun: 1"])

  def test_get_player_basic_stats(self):
    '''Info command should return printout of player's vitals.'''
    result = []
    for output in player_class.test_player.info():
      result.append(output)
    self.assertEqual(result,["Health: 100","Stamina: 100"])


if __name__ == '__main__':
  unittest.main()
