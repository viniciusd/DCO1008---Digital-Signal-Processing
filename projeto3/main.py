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
    ret = np.apply_along_axis(dct, 0, x)
    #print('DCT')
    #print(ret)
    return ret
    
def idct(x):
    return np.round(fftpack.idct(x, norm='ortho'))

def idct2(X):
    ret = np.apply_along_axis(idct, 0, X)
    left = idct(X[:, 0])
    right = idct(X[:, 1])

    #import pdb; pdb.set_trace()
    print('IDCT')
    print('Got:')
    print(X)
    print('Returning:')
    print(ret)
    return ret

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
y2[:,0] = idct(dct2(sig)[:, 0])
y2[:,1] = idct(dct2(sig)[:, 1])


y3 = idct2(dct2(sig))

y = aifc.open('song2.aif', 'wb')
y.setnchannels(x.getnchannels())
y.setsampwidth(x.getsampwidth())
y.setframerate(x.getframerate())
#y.writeframes(idct2(X).flatten().tobytes())
y.writeframes(y2.flatten().tobytes())
