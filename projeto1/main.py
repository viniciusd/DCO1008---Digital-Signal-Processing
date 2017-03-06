#!bin/python3
from scipy import misc
from scipy import signal
import scipy
import numpy as np

from array import UnboundedArray

image = UnboundedArray(misc.imread('lena.png'))
filtered = np.copy(image)
kernel = 1/9*np.ones((3,3))

for (i, j), x in np.ndenumerate(image):
     filtered[i, j] = image[i-1:(i+1)+1, j-1:(j+1)+1].dot(kernel).sum()

sc = scipy.ndimage.filters.convolve(image, kernel)
np.testing.assert_array_equal(filtered, sc)
#print(((filtered - sc) ** 2).mean())
misc.imsave('filtered_lena.png', filtered)
misc.imsave('filtered_lena2.png', sc)
