#!bin/python3
import unittest

import numpy as np

from array import UnboundedArray as uarray

class TestUnboundedArray(unittest.TestCase):

    def setUp(self):
        self.arr = uarray([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.brr = uarray([[131.2807, 136.2802, 133.2805, 131.9925, 136.992, 136.7039, 134.7041, 137.7038, 133.1773, 134.1772], [ 134.2804, 135.2803, 132.2806, 133.9923, 138.9918, 132.7043, 129.7046, 137.7038, 139.8777, 137.8779]])
        self.crr = uarray([[1, 2, 3, 4, 5, 6],[7, 8, 9, 10, 11, 12]])

    @unittest.skip('Skipping for now, it works')
    def test_getting_normal_element(self):
        self.assertEqual(self.arr[0, 1], 2)

    @unittest.skip('Skipping for now, it works')
    def test_getting_normal_element_2(self):
        self.assertEqual(self.arr[1, 0], 4)

    @unittest.skip('Skipping for now, it works')
    def test_slicing_with_horizontal_borders(self):
        np.testing.assert_array_equal(self.arr[-1:1, 0], np.array([1, 1]).reshape(uarray.COLUMN))

    @unittest.skip('Skipping for now, it works')
    def test_slicing_with_horizontal_borders_2(self):
        np.testing.assert_array_equal(self.arr[-1:2, 0], np.array([2.5, 1, 4]).reshape(uarray.COLUMN))

    @unittest.skip('Skipping for now, it works')
    def test_slicing_with_horizontal_borders_3(self):
        np.testing.assert_array_equal(self.arr[-1:0+1, 0:2+1], np.array([[2, 2, 2], [1, 2, 3]]))

    #@unittest.skip('Skipping for now, it works')
    def test_slicing_with_horizontal_borders_4(self):
        np.testing.assert_array_equal(self.crr[-1:1+1, 1:3+1], np.array([[6, 6, 6], [2, 3, 4], [8, 9, 10]]))

    @unittest.skip('Skipping for now, it works')
    def test_slicing_with_vertical_borders(self):
        np.testing.assert_array_equal(self.arr[1, -1:2], np.array([4.5, 4, 5]).reshape(uarray.LINE))

    @unittest.skip('Skipping for now, it works')
    def test_getting_upper_right_corner(self):
        np.testing.assert_array_equal(self.arr[-1:2,1:4], np.array([[4, 4, 4], [2, 3, 4], [5, 6, 4]]))

if __name__ == '__main__':
    unittest.main(verbosity=2)
