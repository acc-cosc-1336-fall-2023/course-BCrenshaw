import unittest

from src.examples.c_decisions.decisions import get_letter_grade, test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_get_letter_grade(self):
        self.assertEqual(get_letter_grade(95), "A")
        self.assertEqual(get_letter_grade(85), "B")
        self.assertEqual(get_letter_grade(75), "C")
        self.assertEqual(get_letter_grade(65), "D")
        self.assertEqual(get_letter_grade(12), "F")
        self.assertEqual(get_letter_grade(400), "E")
        self.assertEqual(get_letter_grade(-5), "E")