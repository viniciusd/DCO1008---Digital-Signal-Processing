#!bin/python3
import unittest

from array import UnboundedArray

class TestUnboundedArray(unittest.TestCase):

    def setUp(self):
        self.arr = UnboundedArray([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_print_normal_element(self):
        self.assertEqual(self.arr[0, 1], 2)

    def test_print_generating_borders(self):
        self.arr[-1:1, -1:1]

if __name__ == '__main__':
    unittest.main(verbosity=2)
