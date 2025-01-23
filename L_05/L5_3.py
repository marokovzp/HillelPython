import string
# print(string.punctuation)

# my_str = 'Python Community'# -> #PythonCommunity
# my_str = 'i like python community!'# -> #ILikePythonCommunity
my_str = 'Should, I. subscribe? Yes!'# -> #ShouldISubscribeYes

print(my_str, end=' ')
print('=>', end=' ')

my_str = my_str.title()
lst = my_str.split()
new_str ="".join(lst)

lst = list(new_str)

for i, el in enumerate (lst):
    for el_punc in string.punctuation:
        if el == el_punc:
            lst.remove(el)

lst.insert(0, '#')

my_len = 140
if len(lst) > my_len:
    lst = (lst[:my_len])

new_str ="".join(lst)

print(new_str)