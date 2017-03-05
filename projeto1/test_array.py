#!bin/python3
import unittest

import numpy as np

from array import UnboundedArray

class TestUnboundedArray(unittest.TestCase):

    def setUp(self):
        self.arr = UnboundedArray([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_getting_normal_element(self):
        self.assertEqual(self.arr[0, 1], 2)

    def test_getting_normal_element_2(self):
        self.assertEqual(self.arr[1, 0], 4)

    @unittest.skip('It is passing, let us skip it while not fixing the other one')
    def test_getting_generating_horizontal_borders(self):
        np.testing.assert_array_equal(self.arr[-1:1, 0], np.array([1, 1, ]).reshape((-1,1)))

    def test_getting_generating_horizontal_borders_2(self):
        np.testing.assert_array_equal(self.arr[-1:2, 0], np.array([2.5, 1, 4]).reshape((-1,1)))

    @unittest.skip('Skipping for now')
    def test_getting_generating_vertical_borders(self):
        self.arr[1, -1:1]

if __name__ == '__main__':
    unittest.main(verbosity=2)
