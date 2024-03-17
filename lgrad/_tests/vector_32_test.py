from lgrad._python.vector import Int32Array, fromList, fromVector
test_arr_1 = [i for i in range(10)]

def test_create():
    arr = Int32Array()
    for i in test_arr_1:
        arr.append(i)
    for i in range(len(arr)):
        # assert arr[i] == test_arr_1
        print(i)

test_create()