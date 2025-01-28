import string
# print(string.ascii_letters)

# my_str = "a-c"# -> abc
# my_str = "a-a"# -> a
# my_str = "s-H"# -> stuvwxyzABCDEFGH
# my_str = "a-A"# -> abcdefghijklmnopqrstuvwxyzA
my_str = input('type two letters with "-": ')

print(my_str, end=' ')
print('=>', end=' ')

for i, el in enumerate(string.ascii_letters):
    if el == my_str[0]:
        start_i = i
    if el == my_str[2]:
        end_i = i
        break

for i, el in enumerate(string.ascii_letters):
    if i >= start_i and i <= end_i:
        print(el, end='')