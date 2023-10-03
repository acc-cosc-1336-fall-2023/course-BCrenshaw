import unittest

from examples.h_strings.strings import slice_string, concat_strings

class Test_Config(unittest.TestCase):

    def test_concat_strings(self):
        self.assertEqual('bluebird', concat_strings('blue', 'bird'))

    def test_slice_string(self):
        self.assertEqual('lynn', slice_string('patty lynn freebush'))