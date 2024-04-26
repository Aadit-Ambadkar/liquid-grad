import ctypes
from lgrad._python.load_so import load_so
from lgrad._python.vector import *

lib = load_so("https://github.com/Aadit-Ambadkar/lg-compiled/raw/main/_arithmetic.so")
lib.z_add_f64.restype = ctypes.c_void_p
lib.z_add_f64.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
lib.o_add_f64.restype = ctypes.c_void_p
lib.o_add_f64.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
lib.z_sub_f64.restype = ctypes.c_void_p
lib.z_sub_f64.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
lib.o_sub_f64.restype = ctypes.c_void_p
lib.o_sub_f64.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
lib.z_mul_f64.restype = ctypes.c_void_p
lib.z_mul_f64.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
lib.o_mul_f64.restype = ctypes.c_void_p
lib.o_mul_f64.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
lib.o_div_f64.restype = ctypes.c_void_p
lib.o_div_f64.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

def f64_add(vec_1: DoubleVector, vec_2: DoubleVector, filler=0):
    if filler == 0:
        return fromVector(lib.z_add_f64(vec_1.vector, vec_2.vector), dtype="float64")
    elif filler == 1:
        return fromVector(lib.o_add_f64(vec_1.vector, vec_2.vector), dtype="float64")
        
def f64_subtract(vec_1: DoubleVector, vec_2: DoubleVector, filler=0):
    if filler == 0:
        return fromVector(lib.z_sub_f64(vec_1.vector, vec_2.vector), dtype="float64")
    elif filler == 1:
        return fromVector(lib.o_sub_f64(vec_1.vector, vec_2.vector), dtype="float64")

def f64_multiply(vec_1: DoubleVector, vec_2: DoubleVector, filler=1):
    if filler == 0:
        return fromVector(lib.z_mul_f64(vec_1.vector, vec_2.vector), dtype="float64")
    elif filler == 1:
        return fromVector(lib.o_mul_f64(vec_1.vector, vec_2.vector), dtype="float64")

def f64_divide(vec_1: DoubleVector, vec_2: DoubleVector, filler=1):
    if filler == 0:
        raise ZeroDivisionError("Cannot have filler be 0 for division")
    elif filler == 1:
        return fromVector(lib.o_div_f64(vec_1.vector, vec_2.vector), dtype="float64")