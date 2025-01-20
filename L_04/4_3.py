import random

list = [random.randint(0, 9) for i in range(random.randint(3, 10))]

new_list = []
new_list.append(list[0])
new_list.append(list[2])
new_list.append(list[len(list) - 2])

print(list, end=' ')
print('==', end=' ')
print(new_list)