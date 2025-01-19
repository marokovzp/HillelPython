user_input = input('Type digits with space: ')

list = []
for item in user_input.split():
    list.append(int(item))

print(list, end=' ')
print('=>', end=' ')

if len(list) > 0:
    last_digit_index = len(list) - 1
    last_digit = list[last_digit_index]
    del (list[last_digit_index])
    list.insert(0, last_digit)
    print(list)
else:
    print ('[]')
