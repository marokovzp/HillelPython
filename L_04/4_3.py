import random

lst = [random.randint(0, 9) for i in range(random.randint(3, 10))]

new_lst = []
new_lst.append(lst[0])
new_lst.append(lst[2])
new_lst.append(lst[len(lst) - 2])

print(lst, end=' ')
print('==', end=' ')
print(new_lst)