#lst = [12, 3, 4, 10]
#lst = [1]
#lst = []
lst = [12, 3, 4, 10, 8]


print(lst, end=' ')
print('=>', end=' ')

if len(lst) > 0:
    last_digit_index = len(lst) - 1
    last_digit = lst[last_digit_index]
    del (lst[last_digit_index])
    lst.insert(0, last_digit)
    print(lst)
else:
    print (lst)
