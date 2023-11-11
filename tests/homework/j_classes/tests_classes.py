import unittest

from src.homework.j_classes.class_a import Die as d

class Test_Config(unittest.TestCase):

    def test_get_rolled_value(self):
        lower_range = 1
        upper_range = 6
        self.assertEqual(lower_range <= d().get_rolled_value() <= upper_range, True)
        self.assertEqual(lower_range <= d().get_rolled_value() <= upper_range, True)
        self.assertEqual(lower_range <= d().get_rolled_value() <= upper_range, True)