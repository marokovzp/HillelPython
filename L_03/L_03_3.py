lst = [1, 2, 3, 4, 5, 6]# => [[1, 2, 3], [4, 5, 6]]
#lst = [1, 2, 3]# => [[1, 2], [3]]
#lst = [1, 2, 3, 4, 5]# => [[1, 2, 3], [4, 5]]
#lst = [1]# => [[1], []]
#lst = []# => [[], []]

if (len(lst) % 2) == 0:
    length_1 = len(lst)/2
    length_2 = length_1
else:
    length_2 = len(lst) // 2
    length_1 = length_2 + 1

lst_1 = lst[:int(length_1)]
lst_2 = lst[int(length_1):int(len(lst))]

new_lst = []
new_lst.append(lst_1)
new_lst.append(lst_2)

print(new_lst)