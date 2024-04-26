from lgrad._python.vector import DoubleVector, fromList
from lgrad._python import math as lmath

test_arr_1 = [i+0.5 for i in range(10)]
test_arr_2 = [i+0.5 for i in range(18789038-10,18789038,2)]

def test_create():
    print("Test Create: ", end="")
    arr = DoubleVector()
    for i in test_arr_1:
        arr.append(i)

    print(len(arr))
    for i in range(len(arr)):
        print(arr[i], end=" ", flush=True)
    print()

    return arr

def test_from_list():
    print("Test fromList: ", end="")
    arr = fromList(test_arr_2, dtype="float64")
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
    return arr

def test_iter():
    print("Test iter: ", end="")
    arr = fromList(test_arr_1, dtype="float64")
    print(*arr, sep=" ")
    return arr

def test_str():
    print("Test str: ", end="")
    arr = fromList(test_arr_1, dtype="float64")
    print(arr)
    return arr

def test_add():
    print("Test addition: ", end="")
    arr1 = fromList(test_arr_1, dtype="float64")
    arr2 = fromList(test_arr_2, dtype="float64")
    res = lmath.f64_add(arr1, arr2)
    print(res)

def test_sub():
    print("Test subtraction: ", end="")
    arr1 = fromList(test_arr_1, dtype="float64")
    arr2 = fromList(test_arr_2, dtype="float64")
    res = lmath.f64_subtract(arr1, arr2)
    print(res)

def test_mul():
    print("Test multiplication: ", end="")
    arr1 = fromList(test_arr_1, dtype="float64")
    arr2 = fromList(test_arr_2, dtype="float64")
    res = lmath.f64_multiply(arr1, arr2)
    print(res)

def test_div():
    print("Test multiplication: ", end="")
    arr1 = fromList(test_arr_1, dtype="float64")
    arr2 = fromList(test_arr_2, dtype="float64")
    res = lmath.f64_divide(arr1, arr2)
    print(res)

test_create()
test_from_list()
test_iter()
test_str()
test_add()
test_sub()
test_mul()
test_div()

"""Test Create: 0 1 2 3 4 5 6 7 8 9 
Test fromList: 10 12 14 16 18 
Test iter: 0 1 2 3 4 5 6 7 8 9
Test str: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Test addition: [10, 13, 16, 19, 22, 5, 6, 7, 8, 9]
Test subtraction: [-10, -11, -12, -13, -14, 5, 6, 7, 8, 9]
Test multiplication: [0, 12, 28, 48, 72, 5, 6, 7, 8, 9]"""