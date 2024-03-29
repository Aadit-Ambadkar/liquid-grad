import ctypes
from lgrad._python.load_so import load_so

class _v32(object):
    lib = load_so("https://github.com/Aadit-Ambadkar/lg-compiled/raw/main/_vector_int32.so")
    lib._create.restype = ctypes.c_void_p
    lib._create.argtypes = []
    lib._delete.restype = None
    lib._delete.argtypes = [ctypes.c_void_p]
    lib._size.restype = ctypes.c_int64
    lib._size.argtypes = [ctypes.c_void_p]
    lib._get.restype = ctypes.c_int32
    lib._get.argtypes = [ctypes.c_void_p, ctypes.c_int]
    lib._push_back.restype = None
    lib._push_back.argtypes = [ctypes.c_void_p, ctypes.c_int32]
    
    def fromList(li):
        arr = Int32Array()
        for i in li:
            arr.append(i)
        return arr

    def fromVector(vec):
        arr = Int32Array()
        arr.vector = vec
        return arr

class _v64(object):
    lib = load_so("https://github.com/Aadit-Ambadkar/lg-compiled/raw/main/_vector_int64.so")
    lib._create.restype = ctypes.c_void_p
    lib._create.argtypes = []
    lib._delete.restype = None
    lib._delete.argtypes = [ctypes.c_void_p]
    lib._size.restype = ctypes.c_int64
    lib._size.argtypes = [ctypes.c_void_p]
    lib._get.restype = ctypes.c_int64
    lib._get.argtypes = [ctypes.c_void_p, ctypes.c_int]
    lib._push_back.restype = None
    lib._push_back.argtypes = [ctypes.c_void_p, ctypes.c_int64]
    
    def fromList(li):
        arr = Int64Array()
        for i in li:
            arr.append(i)
        return arr

    def fromVector(vec):
        arr = Int64Array()
        arr.vector = vec
        return arr



class Int32Array(object):
    def __init__(self):
        self.vector = _v32.lib._create()
    def __del__(self):
        _v32.lib._delete(self.vector)
    def __len__(self):
        return _v32.lib._size(self.vector)
    def __getitem__(self, i):
        if 0 <= i < self.__len__():
            return _v32.lib._get(self.vector, ctypes.c_int(i))
        raise IndexError(f'Index {i} out of range for IntArray with size of {self.__len__()}')
    def __iter__(self):
        for i in range(self.__len__()):
            yield self.__getitem__(i)
    def __repr__(self):
        return f"[{', '.join(str(i) for i in self)}]"
    def append(self, i):
        _v32.lib._push_back(self.vector, ctypes.c_int32(i))

class Int64Array(object):
    def __init__(self):
        self.vector = _v64.lib._create()
    def __del__(self):
        _v64.lib._delete(self.vector)
    def __len__(self):
        return _v64.lib._size(self.vector)
    def __getitem__(self, i):
        if 0 <= i < self.__len__():
            return _v64.lib._get(self.vector, ctypes.c_int(i))
        raise IndexError(f'Index {i} out of range for IntArray with size of {self.__len__()}')
    def __iter__(self):
        for i in range(self.__len__()):
            yield self.__getitem__(i)
    def __repr__(self):
        return f"[{', '.join(str(i) for i in self)}]"
    def append(self, i):
        _v64.lib._push_back(self.vector, ctypes.c_int64(i))



def fromList(li, dtype="int32"):
    if dtype == "int32":
        return _v32.fromList(li)
    elif dtype == "int64":
        return _v64.fromList(li)

def fromVector(vec, dtype="int32"):
    if dtype == "int32":
        return _v32.fromVector(vec)
    elif dtype == "int64":
        return _v64.fromVector(vec)