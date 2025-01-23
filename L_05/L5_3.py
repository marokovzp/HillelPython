import string
# print(string.punctuation)

# my_str = 'Python Community'# -> #PythonCommunity
# my_str = 'i like python community!'# -> #ILikePythonCommunity
# my_str = 'Should, I. subscribe? Yes!'# -> #ShouldISubscribeYes
my_str = input('type your name: ')


print(my_str, end=' ')
print('=>', end=' ')

my_str = my_str.title()
lst = my_str.split()
new_str ="".join(lst)

lst2 = list(new_str)
print(lst2)

lst3 = []
for i, el in enumerate (lst2):
    for el_punc in string.punctuation:
        if el == el_punc:
            lst3.append(i)
for i in reversed(lst3):
    lst2.pop(i)

lst2.insert(0, '#')

my_len = 140
if len(lst2) > my_len:
    lst2 = (lst2[:my_len])

new_str ="".join(lst2)

print(new_str)