import string
import keyword
# print(string.punctuation)
# print(keyword.kwlist)

# my_str = '_'# => True
# my_str = '__'# => False
# my_str = '___'# => False
# my_str = 'x'# => True
# my_str = 'get_value'# => True
# my_str = 'get value'# => False
# my_str = 'get!value'# => False
# my_str = 'some_super_puper_value'# => True
# my_str = 'Get_value'# => False
# my_str = 'get_Value'# => False
# my_str = 'getValue'# => False
# my_str = '3m'# => False
# my_str = 'm3'# => True
# my_str = 'assert'# => False
my_str = 'assert_exception'# => True

# my_str = input('type your string: ')

print(my_str, end=' ')
print('=>', end=' ')

is_False_count = 0
lst = list(my_str)

for i in my_str:
    if i.isupper():
        is_False_count += 1

if lst[0].isdigit():
    is_False_count += 1

for i, el in enumerate (lst):
    for el_punc in string.punctuation:
        if el == el_punc or el == " ":
            if el != "_":
                is_False_count += 1

for i, el in enumerate(keyword.kwlist):
    if my_str.count(el):
        if len(el) == len(my_str):
            is_False_count += 1

if my_str.count("__"):
    is_False_count += 1

print (is_False_count == 0)