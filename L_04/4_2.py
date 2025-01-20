list = [0, 1, 7, 2, 4, 8]# => (0 + 7 + 4) * 8 = 88
# list = [1, 3, 5]# => 30
# list = [6]# => 36
# list = []# => 0

print (list, end=' ')
print('=>', end=' ')

new_list = []

if len(list) > 0:
    last_element = list[len(list) - 1]
else:
    last_element = 0

for i, el in enumerate (list):
    if (i % 2) == 0:
        new_list.append(el)

sum_all = sum(new_list)
rez = sum_all * last_element

print(rez)