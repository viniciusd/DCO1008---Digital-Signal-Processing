import aifc
import sndhdr

import utils

class Aiff:
    def __init__(self, filename):
        assert sndhdr.what(filename).filetype == 'aiff'

        x = aifc.open(filename)

        data = x.readframes(x.getnframes())

        self.nchannels = x.getnchannels()
        self.sampwidth = x.getsampwidth()
        self.framerate = x.getframerate()
        self.sig = utils.from_buffer(data).reshape(-1, x.getnchannels())

    def save(self, filename):
        y = aifc.open('song2.aif', 'wb')
        y.setnchannels(self.nchannels)
        y.setsampwidth(self.sampwidth)
        y.setframerate(self.framerate)
        y.writeframes(self.sig.flatten().tobytes())
