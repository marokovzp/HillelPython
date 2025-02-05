lst_1 = [7]
lst_2 = [5, 8]
lst_3 = [9, 8, 2]
lst_4 = [1, 3, 5, 6]
lst_5 = [6, 2, 4, 4, 5]
lst_6 = [9, 5, 3, 5, 5, 7]
lst_7 = [7, 4, 6, 4, 6, 7, 8] #[7, 4, 6, 4, 7, 6, 8]
lists = [lst_1, lst_2, lst_3, lst_4, lst_5, lst_6, lst_7]

step = 0
my_summ = 0
lst = []
lst_next = []
for i, el in enumerate(lists):
    lst = el
    lst.append(0)
    lst = lst[step:]
    if lst[0] < lst[1]:
        step += 1
    elif lst[0] == lst[1]:
        lst_next = lists[i + 1]
        lst_next = lst_next[step:]
        if lst_next[0] < lst_next[1]:
            step += 1
    my_summ += int(el[step])
    print(my_summ)
print('Result', end=' ')
print(my_summ)