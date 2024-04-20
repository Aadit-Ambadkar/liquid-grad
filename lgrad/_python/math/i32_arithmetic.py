import ctypes
from lgrad._python.load_so import load_so
from lgrad._python.vector import *

lib = load_so("https://github.com/Aadit-Ambadkar/lg-compiled/raw/main/_arithmetic.so")
lib.z_add_i32.restype = ctypes.c_void_p
lib.z_add_i32.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
lib.o_add_i32.restype = ctypes.c_void_p
lib.o_add_i32.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
lib.z_sub_i32.restype = ctypes.c_void_p
lib.z_sub_i32.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
lib.o_sub_i32.restype = ctypes.c_void_p
lib.o_sub_i32.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
lib.z_mul_i32.restype = ctypes.c_void_p
lib.z_mul_i32.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
lib.o_mul_i32.restype = ctypes.c_void_p
lib.o_mul_i32.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

def i32_add(vec_1: Int32Vector, vec_2: Int32Vector, filler=0):
    if filler == 0:
        return fromVector(lib.z_add_i32(vec_1.vector, vec_2.vector), dtype="int32")
    elif filler == 1:
        return fromVector(lib.o_add_i32(vec_1.vector, vec_2.vector), dtype="int32")
        
def i32_subtract(vec_1: Int32Vector, vec_2: Int32Vector, filler=0):
    if filler == 0:
        return fromVector(lib.z_sub_i32(vec_1.vector, vec_2.vector), dtype="int32")
    elif filler == 1:
        return fromVector(lib.o_sub_i32(vec_1.vector, vec_2.vector), dtype="int32")
    
def i32_multiply(vec_1: Int32Vector, vec_2: Int32Vector, filler=1):
    if filler == 0:
        return fromVector(lib.z_mul_i32(vec_1.vector, vec_2.vector), dtype="int32")
    elif filler == 1:
        return fromVector(lib.o_mul_i32(vec_1.vector, vec_2.vector), dtype="int32")