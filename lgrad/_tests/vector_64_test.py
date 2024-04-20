from lgrad._python.vector import Int64Vector, fromList
from lgrad._python import math as lmath

test_arr_1 = [i for i in range(991238-10, 991238)]
test_arr_2 = [i for i in range(1234779-10,1234779,2)]

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

test_create()
test_from_list()
test_iter()
test_str()
test_add()
test_sub()
test_mul()

"""Test Create: 991228 991229 991230 991231 991232 991233 991234 991235 991236 991237 
Test fromList: 1234769 1234771 1234773 1234775 1234777 
Test iter: 991228 991229 991230 991231 991232 991233 991234 991235 991236 991237
Test str: [991228, 991229, 991230, 991231, 991232, 991233, 991234, 991235, 991236, 991237]
Test addition: [2225997, 2226000, 2226003, 2226006, 2226009, 991233, 991234, 991235, 991236, 991237]
Test subtraction: [-243541, -243542, -243543, -243544, -243545, 991233, 991234, 991235, 991236, 991237]
Test multiplication: [1223937606332, 1223940823559, 1223944040790, 1223947258025, 1223950475264, 991233, 991234, 991235, 991236, 991237]"""