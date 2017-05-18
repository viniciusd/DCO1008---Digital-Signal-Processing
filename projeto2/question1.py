#from scipy.fftpack import fft, fftfreq, fftshift
from scipy import fftpack
import numpy as np
import matplotlib.pyplot as plt

class Fft:
    def __init__(self, x, *, sample_rate=None, padded=False):
        if sample_rate == None:
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

def plot(x):
    X = Fft(x, sample_rate=8192, padded=True)
    plt.plot(X.hz, X.abs)
    plt.show()

def fft_time():
    """ Runs scipy's fft a lot of times to estimate its execution time
        As we are running 10**6 times and the timeit function returns
        the cumulate time, our result is the average time in microseconds,
        once we would divide by 10**6 to get the average time and multiple
        it back by 10**6 to get the time in microseconds :)
    """
    import timeit

    setup = """
from scipy.fftpack import fft
from dados import x
import numpy as np
x = np.array(x)
        """
    extra_element = """
x = np.append(x, 0)
        """
    padding = """
n = int(2**np.ceil(np.log2(len(x))))
x = np.pad(x, (0, n-len(x)%n), 'constant')
        """
    return {
            'not-padded': timeit.timeit('fft(x)', setup=setup, number=10**6),
            'prime-padded': timeit.timeit('fft(x)', setup=setup+extra_element, number=10**6),
            '2power-padded': timeit.timeit('fft(x)', setup=setup+padding, number=10**6),
            }

if __name__ == '__main__':
    from dados import x
    print(fft_time())
