# lst  = [0, 1, 0, 12, 3]# -> [1, 12, 3, 0, 0]
# lst  = [0]# -> [0]
# lst  = [1, 0, 13, 0, 0, 0, 5]# -> [1, 13, 5, 0, 0, 0, 0]
lst  = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]# -> [9, 7, 31, 45, 45, 45, 96, 0, 0, 0, 0, 0, 0, 0]

print (lst, end=' ')
print('=>', end=' ')

lst0 = []
del_lst = []

for i, el in enumerate (lst):
    if el == 0:
        lst0.append(el)
        del_lst.append(i)

for i in reversed(del_lst):
    lst.pop(i)
    lst.append(0)

print (lst)