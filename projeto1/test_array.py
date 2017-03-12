#!bin/python3
import unittest

import numpy as np

from array import UnboundedArray as uarray

class TestUnboundedArray(unittest.TestCase):

    def setUp(self):
        self.arr = uarray([[1, 2, 3], [4, 5, 6], [7, 8, 9]], padding='mean')
        self.brr = uarray([[1, 2, 3, 4, 5, 6],[7, 8, 9, 10, 11, 12]], padding='mean')

    def test_getting_normal_element(self):
        self.assertEqual(self.arr[0, 1], 2)

    def test_getting_normal_element_2(self):
        self.assertEqual(self.arr[1, 0], 4)

    def test_slicing_with_horizontal_borders(self):
        np.testing.assert_array_equal(self.arr[-1:1, 0], np.array([1, 1]).reshape(uarray.COLUMN))

    def test_slicing_with_horizontal_borders_2(self):
        np.testing.assert_array_equal(self.arr[-1:2, 0], np.array([2.5, 1, 4]).reshape(uarray.COLUMN))

    def test_slicing_with_horizontal_borders_3(self):
        np.testing.assert_array_equal(self.arr[-1:0+1, 0:2+1], np.array([[2, 2, 2], [1, 2, 3]]))

    def test_slicing_with_horizontal_borders_4(self):
        np.testing.assert_array_equal(self.brr[-1:1+1, 1:3+1], np.array([[6, 6, 6], [2, 3, 4], [8, 9, 10]]))

    def test_slicing_with_vertical_borders(self):
        np.testing.assert_array_equal(self.arr[1, -1:2], np.array([4.5, 4, 5]).reshape(uarray.LINE))

    def test_getting_upper_right_corner(self):
        np.testing.assert_array_equal(self.arr[-1:2,1:4], np.array([[4, 4, 4], [2, 3, 4], [5, 6, 4]]))

if __name__ == '__main__':
    unittest.main(verbosity=2)
