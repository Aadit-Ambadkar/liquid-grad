import ctypes
from lgrad._python.load_so import load_so
from .vector_base import Vector

class _vF64(object):
    lib = load_so("https://github.com/Aadit-Ambadkar/lg-compiled/raw/main/_vector_float64.so")
    lib._create.restype = ctypes.c_void_p
    lib._create.argtypes = []
    lib._delete.restype = None
    lib._delete.argtypes = [ctypes.c_void_p]
    lib._size.restype = ctypes.c_int64
    lib._size.argtypes = [ctypes.c_void_p]
    lib._get.restype = ctypes.c_double
    lib._get.argtypes = [ctypes.c_void_p, ctypes.c_int]
    lib._push_back.restype = None
    lib._push_back.argtypes = [ctypes.c_void_p, ctypes.c_double]
    lib._from_arr.restype = ctypes.c_void_p
    lib._from_arr.argtypes = [ctypes.c_void_p, ctypes.c_int]
    
    def fromList(li):
        arr = DoubleVector()
        arr.populate(li)
        return arr

    def fromVector(vec):
        arr = DoubleVector()
        arr.vector = vec
        return arr

class DoubleVector(Vector):
    def __init__(self):
        self.vector = _vF64.lib._create()
        self.dtype = "float64"
    def __del__(self):
        pass
        # _vF64.lib._delete(self.vector)
    def __len__(self):
        return _vF64.lib._size(self.vector)
    def __getitem__(self, i):
        if 0 <= i < self.__len__():
            return _vF64.lib._get(self.vector, ctypes.c_int(i))
        raise IndexError(f'Index {i} out of range for IntArray with size of {self.__len__()}')
    def __iter__(self):
        for i in range(self.__len__()):
            yield self.__getitem__(i)
    def __repr__(self):
        return f"[{', '.join(str(i) for i in self)}]"
    def populate(self, li):
        self.vector = _vF64.lib._from_arr((ctypes.c_double * len(li))(*li), ctypes.c_int(len(li)))
    def append(self, i):
        _vF64.lib._push_back(self.vector, ctypes.c_double(i))