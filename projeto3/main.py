from aiff import Aiff
import utils

threshold = 1*10**1

sound = Aiff('song.aif')

y2 = utils.dct2(sound.sig)

n= 10
y2[-n:, 0] = 0
y2[-n:, 1] = 0
y2[utils.abs(y2) < threshold] = 0

import numpy as np; import pdb; pdb.set_trace()

y2 = utils.idct2(y2, dtype=sound.sig.dtype)

print(utils.mutual_info(sound.sig, y2))

sound.sig = y2
sound.save('sound2.aif')
