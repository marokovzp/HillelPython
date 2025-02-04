def find_gold(lst):
    lst.append(0)
    if lst[0] >= lst[1]:
        position = 0
    else:
        position = 1
    # lst = lst[position:]
    return position

lst_1 = [7]
lst_2 = [5, 8]
lst_3 = [9, 8, 2]
lst_4 = [1, 3, 5, 6]
lst_5 = [6, 2, 4, 4, 5]
lst_6 = [9, 5, 3, 5, 5, 7]
lst_7 = [7, 4, 6, 4, 7, 6, 8]
lists = [lst_1, lst_2, lst_3, lst_4, lst_5, lst_6, lst_7]
# print(lists)

step = 0
lst = []
my_summ = 0
for i, el in enumerate(lists):
    lst = el
    lst = lst[step:]
    step += find_gold(lst)
    my_summ += int(el[step])
    print(my_summ)
print('Result', end=' ')
print(my_summ)