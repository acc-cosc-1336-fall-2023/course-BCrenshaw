import unittest

from src.homework.g_lists_and_tuples.lists import add_inventory, remove_inventory_widget, state_global_widget_dictionary

class Test_Config(unittest.TestCase):

    def test_add_inventory(self):
        name = 'widget1'
        add_inventory(name, 10)
        self.assertEqual({name: 10}, state_global_widget_dictionary())
        add_inventory(name, 25)
        self.assertEqual({name: 35}, state_global_widget_dictionary())
        add_inventory(name, -10)
        self.assertEqual({name: 25}, state_global_widget_dictionary())

    def test_remove_inventory_widget(self):
        name1 = 'widget1'
        name2 = 'widget2'
        quantity1 = 20
        quantity2 = 25
        add_inventory(name1, quantity1)
        add_inventory(name2, quantity2)
        remove_inventory_widget(name1)
        self.assertEqual(1, len(state_global_widget_dictionary()))