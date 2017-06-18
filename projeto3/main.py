import aifc
import sndhdr

import numpy as np
from scipy import fftpack 
from sklearn.metrics import normalized_mutual_info_score

filename = 'song.aif'
threshold = 2*10**1

assert sndhdr.what(filename).filetype == 'aiff'

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

x = aifc.open(filename)

data = x.readframes(x.getnframes())
sig = np.frombuffer(data, dtype='<i2').reshape(-1, x.getnchannels())
del data

y2 = dct2(sig)
y2[np.abs(y2) < threshold] = 0
y2 = idct2(y2, dtype=sig.dtype)

print(mutual_info(sig, y2))

#import pdb; pdb.set_trace()
y = aifc.open('song2.aif', 'wb')
y.setnchannels(x.getnchannels())
y.setsampwidth(x.getsampwidth())
y.setframerate(x.getframerate())
y.writeframes(y2.flatten().tobytes())
