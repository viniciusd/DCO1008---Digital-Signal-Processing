#!bin/python3
import itertools as iter

import scipy
import numpy as np
from skimage.measure import compare_ssim
import matplotlib.pylab as plt


from array import UnboundedArray


def rgb2gray(rgb):
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    # Scipy implements: r * 299/1000 + g * 587/1000 + b * 114/1000
    # that is the ITU-R 601-2 luma transform
    # Note there is a subtle difference for the r factor, which is
    # matlab's (NTSC/PAL) implementation
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

    return gray

def to_image(arr):
    return scipy.misc.toimage(arr, cmin=0)

web_lena = scipy.misc.imread('lena.png').astype(float)
sigaa_lena = rgb2gray(scipy.misc.imread('lena.bmp', mode='RGB')).astype(float)

kernel1 = 1/9*np.ones((3,3))
kernel2 = np.array([[0,1,0], [1, -4, 1], [0, 1, 0]])

for k, kernel in enumerate((kernel1, kernel2)):
    for im, lena in enumerate((web_lena, sigaa_lena)):
        lenas_name = ('web', 'sigaa')[im]+('_a', '_b')[k]+'_filtered_lena'

        sc = to_image(scipy.ndimage.filters.convolve(lena, kernel))
        sc.save('scipy_'+lenas_name+'.png')
        for padding in ('zero', 'mean'):
            image = UnboundedArray(lena, padding=padding)

            filtered = np.zeros(image.shape)
            for (i, j), x in np.ndenumerate(image):
                 filtered[i, j] = image[i-1:(i+1)+1, j-1:(j+1)+1].dot(kernel).sum()

            filtered = to_image(filtered)
            filtered.save(padding+'_'+lenas_name+'.png')

            ssim = round(compare_ssim(scipy.misc.fromimage(filtered), scipy.misc.fromimage(sc)), 5)
            print(lenas_name+'\n    SSIM '+str(ssim))
