def add_one(some_list):
    my_str = ""
    lst = []

    for el in some_list:
        my_str += str(el)
    my_str = str(int(my_str) + 1)

    for el in my_str:
        lst.append(int(el))

    return lst


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
