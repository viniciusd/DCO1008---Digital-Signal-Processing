#!bin/python3
import numpy as np


class UnboundedArray(np.ndarray):

    def __new__(cls, input_array):
        return np.asarray(input_array).view(cls)

    def _generate_bounds(self, arr, item):
        print(arr)

        for axis, x in ((axis, x) for axis, x in enumerate(item) if isinstance(x, slice)):
            p = -x.start if x.start < 0 else 0
            q = x.stop-2 if x.stop > 2 else 0
            # print(p,q)
            if axis == 0:
                if p:
                    arr = np.vstack((np.array([[arr.mean()]*(arr.shape[axis]), ]*p).reshape((1, -1)),
                                     arr)
                                    )
                if q:
                    arr = np.vstack((arr,
                                     (np.array([[arr.mean()]*(arr.shape[axis]), ]*q).reshape((1, -1))))
                                    )
            elif axis == 1:
                if p:
                    foo = np.array([[arr.mean()]*(arr.shape[axis]), ]*p).reshape((-1,1))
                    arr = np.hstack((np.array([[arr.mean()]*(arr.shape[axis]), ]*p).reshape((-1, 1)),
                                     arr)
                                    )
                if q:
                    arr = np.hstack((arr,
                                     (np.array([[arr.mean()]*(arr.shape[axis]), ]*q).reshape((-1, 1))))
                                    )
        return arr

    def __getitem__(self, item):
        if len(item) > 2:
            raise NotImplementedError

        bounds = tuple(slice(max(x.start, 0), min(x.stop, size), x.step) if isinstance(x, slice) else x for x, size in zip(item, self.shape))
        arr = super().__getitem__(bounds)
        arr = np.array(arr)
        if arr.ndim == 1:
            if isinstance(bounds[0], slice):
                arr = arr.reshape((-1,1))
            elif isinstance(bounds[1], slice):
                arr = arr.reshape((1,-1))

        if bounds != item:
            arr = self._generate_bounds(arr, item)

        return arr

    def __str__(self):
        return str(np.array(self))

    def __repr__(self):
        return str(np.array(self))
