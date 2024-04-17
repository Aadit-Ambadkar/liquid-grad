from lgrad._python.vector import Int64Vector, fromList
from lgrad._python import math as lmath

test_arr_1 = [i for i in range(10)]
test_arr_2 = [i for i in range(10,20,2)]

def test_create():
    print("Test Create: ", end="")
    arr = Int64Vector()
    for i in test_arr_1:
        arr.append(i)
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

    return arr

def test_from_list():
    print("Test fromList: ", end="")
    arr = fromList(test_arr_2, dtype="int64")
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
    return arr

def test_iter():
    print("Test iter: ", end="")
    arr = fromList(test_arr_1, dtype="int64")
    print(*arr, sep=" ")
    return arr

def test_str():
    print("Test str: ", end="")
    arr = fromList(test_arr_1, dtype="int64")
    print(arr)
    return arr

def test_add():
    print("Test addition: ", end="")
    arr1 = fromList(test_arr_1, dtype="int64")
    arr2 = fromList(test_arr_2, dtype="int64")
    res = lmath.i64_add(arr1, arr2)
    print(res)

def test_sub():
    print("Test subtraction: ", end="")
    arr1 = fromList(test_arr_1, dtype="int64")
    arr2 = fromList(test_arr_2, dtype="int64")
    res = lmath.i64_subtract(arr1, arr2)
    print(res)

def test_mul():
    print("Test multiplication: ", end="")
    arr1 = fromList(test_arr_1, dtype="int64")
    arr2 = fromList(test_arr_2, dtype="int64")
    res = lmath.i64_multiply(arr1, arr2)
    print(res)

test_create() # 0 1 2 3 4 5 6 7 8 9
test_from_list() # 10 12 14 16 18 
test_iter() # 0 1 2 3 4 5 6 7 8 9
test_str() # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
test_add() # [10, 13, 16, 19, 22, 5, 6, 7, 8, 9]
test_sub() # [-10, -11, -12, -13, -14, 5, 6, 7, 8, 9]
test_mul() # [0, 12, 28, 48, 72, 0, 0, 0, 0, 0]