import numpy as np
from scipy import fftpack 
from sklearn.metrics import normalized_mutual_info_score


def mutual_info(x, y):
    return normalized_mutual_info_score(x.flatten(), y.flatten())

def dct(x):
    return fftpack.dct(x, norm='ortho')

def dct2(x):
    return np.apply_along_axis(dct, 0, x)

def idct(X, dtype=None):
    return np.round(fftpack.idct(X, norm='ortho'))

def idct2(X, dtype='float'):
    return np.apply_along_axis(idct, 0, X).astype(dtype)

def zeros(arr):
    return np.zeros(arr.shape, dtype=arr.dtype)

def from_buffer(data):
    return np.frombuffer(data, dtype='<i2')

def abs(x):
    return np.abs(x)

def map(func, x):
    return np.array([func(i) for i in x], dtype=x.dtype)
