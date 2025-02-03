def find_unique_value(some_list):
    some_list.sort()
    previous = -1
    uniq_lst = []
    for i, el in enumerate(some_list):
        if el != previous:
            previous = el
            uniq_lst.append(el)

    for i, el in enumerate(uniq_lst):
        some_list.remove(el)

    num = set(uniq_lst).symmetric_difference(set(some_list))
    return float(str(num.pop()))


assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")