#!bin/python3
from scipy import misc
from scipy import signal
import scipy
import numpy as np

from array import UnboundedArray

def rgb2gray(rgb):
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    # Scipy implements: r * 299/1000 + g * 587/1000 + b * 114/1000
    # that is the ITU-R 601-2 luma transform
    # Note there is a subtle difference for the r factor, which is
    # matlab's (NTSC/PAL) implementation
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

    return gray

#image = UnboundedArray(scipy.ndimage.imread('lena.png').astype(float))
image = UnboundedArray(misc.imread('lena.png').astype(float))
image = UnboundedArray(rgb2gray(misc.imread('lena.bmp', mode='RGB')).astype(float))

filtered = np.copy(image)
kernel1 = 1/9*np.ones((3,3))
kernel2 =  np.array([[0,1,0], [1, -4, 1], [0, 1, 0]])

for kernel in (kernel1, kernel2):
    for (i, j), x in np.ndenumerate(image):
         filtered[i, j] = image[i-1:(i+1)+1, j-1:(j+1)+1].dot(kernel).sum()

    misc.imsave('filtered_lena.png', filtered)

    sc = scipy.ndimage.filters.convolve(image, kernel)
    #np.testing.assert_array_equal(filtered, sc)
    print(((filtered - sc) ** 2).mean())
    misc.imsave('filtered_lena2.png', sc)
