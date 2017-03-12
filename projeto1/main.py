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


def subplot_image(image, title='', row_label=''):
    global subplot
    n = next(subplot)
    axs = plt.subplot(2, 2, n)
    axs.get_xaxis().set_ticks([]) #set_visible(False)
    axs.get_yaxis().set_ticks([]) #set_visible(False)
    if n%2 == 1:
        axs.set_ylabel(row_label, rotation=0, size='large')
    axs.set_title(title)
    plt.imshow(image, cmap='gray')


web_lena = scipy.misc.imread('lena.png')
sigaa_lena = rgb2gray(scipy.misc.imread('lena.bmp', mode='RGB'))

kernel1 = 1/9*np.ones((3,3))
kernel2 = np.array([[0,1,0], [1, -4, 1], [0, 1, 0]])
for k, kernel in enumerate((kernel1, kernel2)):
    for im, image in enumerate((web_lena, sigaa_lena)):
        plt.figure()
        subplot = iter.count(1)
        for padding in ('zero', 'mean'):
            image = UnboundedArray(image.astype(float), padding=padding)

            filtered = np.zeros(image.shape)
            for (i, j), x in np.ndenumerate(image):
                 filtered[i, j] = image[i-1:(i+1)+1, j-1:(j+1)+1].dot(kernel).sum()

            filtered = scipy.misc.toimage(filtered, cmin=0)
            filtered.save(padding+str(('_web', '_sigaa')[im])+str(k+1)+'filtered_lena.png')

            sc = scipy.ndimage.filters.convolve(image, kernel)
            sc = scipy.misc.toimage(sc, cmin=0)
            sc.save(padding+str(('_web', '_sigaa')[im])+str(k+1)+'filtered_lena2.png')


            ssim = 'SSIM\n'+str(round(compare_ssim(scipy.misc.fromimage(filtered), scipy.misc.fromimage(sc)), 3))
            print(ssim)
            subplot_image(filtered, padding+str(('_web', '_sigaa')[im])+str(k+1)+'filtered_lena.png', row_label=ssim)
            subplot_image(sc)

#plt.imshow(filtered, cmap='gray')
plt.tight_layout()
plt.show()
