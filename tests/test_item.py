import unittest
from modules import item

class ItemTests(unittest.TestCase):

  def test_blank(self):
    pass


class ItemBuilderHelperTests(unittest.TestCase):

  def test_item_object_builder(self):
    '''Item has correct attributes name, description, carry, weight, breakable, & damage when using the helper function'''
    test_item = item.item_builder(("Gun","M4 Machine Gun", True, 10, False, 60))
    self.assertTrue(isinstance(test_item, item.Item))
    self.assertEqual([test_item.name, test_item.descrip, test_item.carry, test_item.weight, test_item.breakable, test_item.damage],["Gun","M4 Machine Gun", True, 10, False, 60])

if __name__ == '__main__':
  unittest.main()
