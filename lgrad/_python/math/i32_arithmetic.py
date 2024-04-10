import ctypes
from lgrad._python.load_so import load_so
from lgrad._python.vector import *

lib = load_so("https://github.com/Aadit-Ambadkar/lg-compiled/raw/main/_arithmetic.so")
lib.z_add_i32.restype = ctypes.c_void_p
lib.z_add_i32.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

def i32_add(vec_1: Int32Vector, vec_2: Int32Vector):
    return fromVector(lib.z_add_i32(vec_1.vector, vec_2.vector), dtype="int32")