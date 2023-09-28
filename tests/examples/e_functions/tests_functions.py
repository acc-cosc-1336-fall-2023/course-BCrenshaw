import unittest

from src.examples.e_functions.value_return_functions import global_variable, global_variable_w_param, local_function_variable, test_config

val3 = 5

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_local_function_variable(self):
        val = 0
        local_function_variable(val) #function called and then closed. Two situations of val but this one closes before the later evaluation.

        self.assertEqual(val, 0)

    def test_global_variable_w_param(self):
        global_variable_w_param(val3)
        self.assertEquals(val3, 5)