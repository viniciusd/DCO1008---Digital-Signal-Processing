#!bin/python3
import numpy as np


class UnboundedArray(np.ndarray):
    COLUMN = (-1, 1)
    LINE = (1, -1)

    def __new__(cls, input_array, padding):
        return np.asarray(input_array).view(cls)

    def __init__(self, input_array, *, padding='zero'):
        if input_array.ndim > 2:
            raise NotImplementedError('3+ dimensions not supported')
        if padding == 'mean':
            self.padding = 1
        elif padding == 'zero':
            self.padding = 0
        else:
            raise NotImplementedError(padding+' padding not implemented. Options are: mean, zero')

    def _generate_bounds(self, arr, item):
        for axis, x in ((axis, x) for axis, x in enumerate(item) if isinstance(x, slice)):
            p = -x.start if x.start < 0 else 0
            q = x.stop-self.shape[axis] if x.stop > self.shape[axis] else 0
            stack = (np.vstack, np.hstack)[axis]
            shape = arr.shape[not axis]
            _1dshape = (self.LINE, self.COLUMN)[axis]
            arr = stack((np.array([[arr.mean()*self.padding]*(shape), ]*p).reshape(_1dshape),
                         arr)
                        ) if p else arr
            arr = stack((arr,
                         (np.array([[arr.mean()*self.padding]*(shape), ]*q).reshape(_1dshape)))
                        ) if q else arr
        return arr

    def __getitem__(self, item):
        bounds = tuple(slice(max(x.start, 0), min(x.stop, size), x.step) if isinstance(x, slice) else x for x, size in zip(item, self.shape))
        arr = super().__getitem__(bounds)
        arr = np.array(arr)
        if arr.ndim == 1:
            if isinstance(bounds[0], slice):
                arr = arr.reshape(self.COLUMN)
            elif isinstance(bounds[1], slice):
                arr = arr.reshape(self.LINE)
        if bounds != item:
            arr = self._generate_bounds(arr, item)
        return arr

    def __str__(self):
        return str(np.array(self))

    def __repr__(self):
        return str(np.array(self))
