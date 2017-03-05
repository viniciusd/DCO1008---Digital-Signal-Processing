#!bin/python3
import unittest

from array import UnboundedArray

a = UnboundedArray([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a[0, 1])
print(a[-1:1, -1:1])
