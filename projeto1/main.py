#!bin/python3
from scipy import misc
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

image = UnboundedArray(rgb2gray(misc.imread('lena.bmp', mode='RGB')))
#image = misc.imread('lena.bmp', mode='L')
misc.imsave('grey_lena.bmp', image)
#print(image)
filtered = np.copy(image)
kernel = 1/9*np.ones((3,3))

for (i, j), x in np.ndenumerate(image):
    print((i,j))
    #filtered[i, j] = image[i-1:i+1, j-1:j+1].dot(kernel).sum()
    if i or j:
        print(image[i-1:i+1+1, j-1:j+1+1])
        input()

# import matplotlib.pyplot as plt
# plt.imshow(rgb2gray(image))
# plt.show()
