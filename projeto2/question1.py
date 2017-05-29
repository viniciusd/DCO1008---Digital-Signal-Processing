from pprint import pprint

import matplotlib.pyplot as plt

from common import Fft


def fft_padded_plot(x):
    X = Fft(x, sample_rate=8192, padded=True)
    plt.figure()
    plt.plot(X.hz, X.abs)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('|H|')
    plt.savefig('q1_fft_padded.png')


def fft_not_padded_plot(x):
    X = Fft(x, sample_rate=8192, padded=False)
    plt.figure()
    plt.plot(X.hz, X.abs)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('|H|')
    plt.savefig('q1_fft_not_padded.png')


def time_plot(x):
    plt.figure()
    plt.plot(x)
    plt.xlabel('Sample')
    plt.ylabel('x')
    plt.savefig('q1_time.png')


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
    fft_padded_plot(x)
    fft_not_padded_plot(x)
    time_plot(x)
    pprint(fft_time())
