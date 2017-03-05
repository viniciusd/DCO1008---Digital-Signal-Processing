#!bin/python3
import numpy as np


class UnboundedArray(np.ndarray):

    def __new__(cls, input_array):
        return np.asarray(input_array).view(cls)

    def _generate_bounds(self, arr, item):
        print(item)
        print(arr)
        if len(item) > 2:
            raise NotImplementedError

        for axis, x in ((axis, x) for axis, x in enumerate(item) if isinstance(x, slice)):
            p, q = -x.start if x.start < 0 else 0, x.stop-1 if x.stop > 1 else 0
            if axis == 0:
                print('axis '+str(axis)+' \n p '+str(p)+' ; q '+str(q))
                print(np.array([[arr.mean()]*(arr.shape[axis]), ]*p).reshape((1, -1)))
                if p:
                    arr = np.vstack((np.array([[arr.mean()]*(arr.shape[axis]), ]*p).reshape((1, -1)),
                             arr)
                             )
                if q:
                    arr = np.vstack((arr,
                             (np.array([[arr.mean()]*(arr.shape[axis]), ]*q).reshape((1, -1))))
                             )
            elif axis == 1:
                print('axis '+str(axis)+' \n p '+str(p)+' ; q '+str(q))
                print(np.array([[arr.mean()]*(arr.shape[axis]), ]*p).reshape((-1, 1)))
                if p:
                    arr = hstack((np.array([[arr.mean()]*(arr.shape[axis]), ]*p).reshape((-1, 1)),
                                 arr)
                                 ) if p else arr
                if q:
                    arr = hstack((arr,
                                 (np.array([[arr.mean()]*(arr.shape[axis]), ]*q).reshape((-1, 1))))
                                 ) if q else arr
        return arr

    def __getitem__(self, item):
        bounds = tuple(slice(max(x.start, 0), min(x.stop, size), x.step) if isinstance(x, slice) else x for x, size in zip(item, self.shape))
        arr = super().__getitem__(bounds)
        if bounds != item:
            arr = self._generate_bounds(arr, item)
        return arr

    def __str__(self):
        return str(np.array(self))

    def __repr__(self):
        return str(np.array(self))

a = UnboundedArray([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(a[0, 1])
#print(a[-1:1, -1:1])
