import unittest

from src.examples.g_lists_and_tuples.lists import get_list_total_for, get_list_total_while, test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_get_list_total_while(self):
        list1 = [5, 10, 20]
        self.assertEqual(get_list_total_while(list1), 35)

    def test_get_list_total_for(self):
        list1 = [5, 10, 20]
        self.assertEqual(get_list_total_for(list1), 35)



