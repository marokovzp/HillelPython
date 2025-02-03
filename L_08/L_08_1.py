def add_one(some_list):
    my_str = ""
    my_str_2 = ""
    lst = []

    for el in some_list:
        my_str += str(el)
    my_summ = int(my_str) + 1
    my_str = str(my_summ)

    for el in my_str:
        lst.append(int(el))

    return lst


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
