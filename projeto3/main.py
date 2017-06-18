from scipy import fftpack 
import aifc
import numpy as np
import sndhdr

filename = 'song.aif'
threshold = 10**-3

assert sndhdr.what(filename).filetype == 'aiff'

def dct(x):
    return fftpack.dct(x, norm='ortho')#.astype(x.dtype)

def dct2(x):
    ret = np.apply_along_axis(dct, 0, x)
    #print('DCT')
    #print(ret)
    return ret
    
def idct(X, dtype=None):
    return np.round(fftpack.idct(X, norm='ortho'))#.astype(X.dtype)

def idct2(X, dtype=None):
    if dtype is None:
        dtype = 'foat'
    return np.apply_along_axis(idct, 0, X).astype(dtype)

def zeros(arr):
    return np.zeros(arr.shape, dtype=arr.dtype)

x = aifc.open('song.aif')

data = x.readframes(x.getnframes())
sig = np.frombuffer(data, dtype='<i2').reshape(-1, x.getnchannels())
x2 = np.copy(sig)

#x2 = dct2(sig)
x2[:,0] = dct(x2[:, 0])
x2[:,1] = dct(x2[:, 1])

y2 = zeros(sig)
mydct = dct2(sig)
#y2[:,0] = idct(mydct[:, 0])
#y2[:,1] = idct(mydct[:, 1])

y2 = np.apply_along_axis(idct, 0, dct2(sig)).astype(y2.dtype)

y3 = zeros(sig)
y3 = idct2(dct2(sig), dtype=sig.dtype)

y = aifc.open('song2.aif', 'wb')
y.setnchannels(x.getnchannels())
y.setsampwidth(x.getsampwidth())
y.setframerate(x.getframerate())
#y.writeframes(idct2(X).flatten().tobytes())
y.writeframes(y3.flatten().tobytes())
