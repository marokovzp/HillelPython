#list = [12, 3, 4, 10]
#list = [1]
#list = []
list = [12, 3, 4, 10, 8]


print(list, end=' ')
print('=>', end=' ')

if len(list) > 0:
    last_digit_index = len(list) - 1
    last_digit = list[last_digit_index]
    del (list[last_digit_index])
    list.insert(0, last_digit)
    print(list)
else:
    print (list)
