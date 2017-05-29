import numpy as np
from scipy import fftpack


class Fft:
    def __init__(self, x, *, sample_rate=None, padded=False):
        if sample_rate is None:
            raise ValueError('You must determine the sample rate')

        fs = sample_rate

        if padded:
            padding_to = int(2**np.ceil(np.log2(len(x))))
            x = np.pad(x, (0, padding_to-len(x)), 'constant')

        n, X = len(x), fftpack.fft(x)

        self.hz = fftpack.fftshift(fftpack.fftfreq(n, 1/fs))
        self.abs = np.abs(X)
        self.phase = np.angle(X)
        self.values = X
        self.samles = n
