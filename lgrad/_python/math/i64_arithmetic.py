import ctypes
from lgrad._python.load_so import load_so
from lgrad._python.vector import *

lib = load_so("https://github.com/Aadit-Ambadkar/lg-compiled/raw/main/_arithmetic.so")
lib.z_add_i64.restype = ctypes.c_void_p
lib.z_add_i64.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
lib.z_sub_i64.restype = ctypes.c_void_p
lib.z_sub_i64.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
lib.z_mul_i64.restype = ctypes.c_void_p
lib.z_mul_i64.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

def i64_add(vec_1: Int64Vector, vec_2: Int64Vector):
    return fromVector(lib.z_add_i64(vec_1.vector, vec_2.vector), dtype="int64")
def i64_subtract(vec_1: Int64Vector, vec_2: Int64Vector):
    return fromVector(lib.z_sub_i64(vec_1.vector, vec_2.vector), dtype="int64")
def i64_multiply(vec_1: Int64Vector, vec_2: Int64Vector):
    return fromVector(lib.z_mul_i64(vec_1.vector, vec_2.vector), dtype="int64")