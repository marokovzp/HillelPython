import string

# my_num = 999# -> 2 # Ось чому - 999 розбиваємо на цифри і перемножуємо 9 * 9 * 9 = 729, Потім 7 * 2 * 9 = 126, потім 1 * 2 * 6 = 12 і в результаті 1 * 2 = 2
# my_num = 1000# -> 0
# my_num = 423# -> 8
# my_num = 33# -> 9
# my_num = 25# -> 0
# my_num = 1# -> 1
my_num = input('input digits: ')

print(my_num, end=' ')
print('->', end=' ')

lst = []
work = 1

while work:
    for el in str(my_num):
        lst.append(el)

    if len(lst) == 1:
        work = 0
        break

    my_num = 1
    for i, el in enumerate(lst):
        my_num *= int(el)

    lst = []

print(my_num)