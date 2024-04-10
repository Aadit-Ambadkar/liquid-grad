from lgrad._python.vector import Int32Vector, fromList
test_arr_1 = [i for i in range(10)]
test_arr_2 = [i for i in range(10,20)]

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

test_create()
test_from_list()



