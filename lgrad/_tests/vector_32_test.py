from lgrad._python.vector import Int32Vector, fromList
from lgrad._python import math as lmath

test_arr_1 = [i for i in range(10)]
test_arr_2 = [i for i in range(10,20,2)]

def test_create():
    print("Test Create: ", end="")
    arr = Int32Vector()
    for i in test_arr_1:
        arr.append(i)
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

    return arr

def test_from_list():
    print("Test fromList: ", end="")
    arr = fromList(test_arr_2)
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
    return arr

def test_iter():
    print("Test iter: ", end="")
    arr = fromList(test_arr_1)
    print(*arr, sep=" ")
    return arr

def test_str():
    print("Test str: ", end="")
    arr = fromList(test_arr_1)
    print(arr)
    return arr

def test_add():
    print("Test addition: ", end="")
    arr1 = fromList(test_arr_1)
    arr2 = fromList(test_arr_2)
    res = lmath.i32_add(arr1, arr2)
    print(res)

def test_sub():
    print("Test subtraction: ", end="")
    arr1 = fromList(test_arr_1)
    arr2 = fromList(test_arr_2)
    res = lmath.i32_subtract(arr1, arr2)
    print(res)

def test_mul():
    print("Test multiplication: ", end="")
    arr1 = fromList(test_arr_1)
    arr2 = fromList(test_arr_2)
    res = lmath.i32_multiply(arr1, arr2)
    print(res)

test_create()
test_from_list()
test_iter()
test_str()
test_add()
test_sub()
test_mul()

"""Test Create: 0 1 2 3 4 5 6 7 8 9 
Test fromList: 10 12 14 16 18 
Test iter: 0 1 2 3 4 5 6 7 8 9
Test str: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Test addition: [10, 13, 16, 19, 22, 5, 6, 7, 8, 9]
Test subtraction: [-10, -11, -12, -13, -14, 5, 6, 7, 8, 9]
Test multiplication: [0, 12, 28, 48, 72, 5, 6, 7, 8, 9]"""