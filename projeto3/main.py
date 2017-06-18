from scipy import fftpack 
import aifc
import numpy as np
import sndhdr

filename = 'song.aif'
threshold = 10**-3

assert sndhdr.what(filename).filetype == 'aiff'

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

x = aifc.open('song.aif')

data = x.readframes(x.getnframes())
sig = np.frombuffer(data, dtype='<i2').reshape(-1, x.getnchannels())

y2 = idct2(dct2(sig), dtype=sig.dtype)

y = aifc.open('song2.aif', 'wb')
y.setnchannels(x.getnchannels())
y.setsampwidth(x.getsampwidth())
y.setframerate(x.getframerate())
y.writeframes(y2.flatten().tobytes())
