lst = [0, 1, 7, 2, 4, 8]# => (0 + 7 + 4) * 8 = 88
# lst = [1, 3, 5]# => 30
# lst = [6]# => 36
# lst = []# => 0

print (lst, end=' ')
print('=>', end=' ')

new_lst = []

if len(lst) > 0:
    last_element = lst[len(lst) - 1]
else:
    last_element = 0

for i, el in enumerate (lst):
    if (i % 2) == 0:
        new_lst.append(el)

sum_all = sum(new_lst)
rez = sum_all * last_element

print(rez)