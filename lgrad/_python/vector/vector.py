import ctypes
from lgrad._python.load_so import load_so
from .vector32 import _v32
from .vector64 import _v64
from .vectorF64 import _vF64

def fromList(li, dtype="int32"):
    if dtype == "int32":
        return _v32.fromList(li)
    elif dtype == "int64":
        return _v64.fromList(li)
    elif dtype == "float64":
        return _vF64.fromList(li)

def fromVector(vec, dtype="int32"):
    if dtype == "int32":
        return _v32.fromVector(vec)
    elif dtype == "int64":
        return _v64.fromVector(vec)
    elif dtype == "float64":
        return _vF64.fromVector(vec)