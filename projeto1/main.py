#!bin/python3
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

kernel1 = 1/9*np.ones((3,3))
kernel2 = np.array([[0,1,0], [1, -4, 1], [0, 1, 0]])

for padding in ('zero', 'mean'):
    web_image = UnboundedArray(scipy.misc.imread('lena.png').astype(float), padding=padding)
    sigaa_image = UnboundedArray(rgb2gray(scipy.misc.imread('lena.bmp', mode='RGB')).astype(float), padding=padding)

    for im, image in enumerate((web_image, sigaa_image)):
        for k, kernel in enumerate((kernel1, kernel2)):
            filtered = np.zeros(image.shape)
            for (i, j), x in np.ndenumerate(image):
                 filtered[i, j] = image[i-1:(i+1)+1, j-1:(j+1)+1].dot(kernel).sum()

            filtered = scipy.misc.toimage(filtered, cmin=0)
            filtered.save(padding+str(('_web', '_sigaa')[im])+str(k+1)+'filtered_lena.png')

            sc = scipy.ndimage.filters.convolve(image, kernel)
            sc = scipy.misc.toimage(sc, cmin=0)

            print(compare_ssim(scipy.misc.fromimage(filtered), scipy.misc.fromimage(sc)))
            sc.save(padding+str(('_web', '_sigaa')[im])+str(k+1)+'filtered_lena2.png')

plt.imshow(filtered, cmap='gray')
cur_axes = plt.gca()
cur_axes.axes.get_xaxis().set_visible(False)
cur_axes.axes.get_yaxis().set_visible(False)
plt.show()
