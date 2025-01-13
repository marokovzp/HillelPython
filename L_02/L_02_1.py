user_input = input('Type 4 digits: ')
print('You inputed next digits:')

input = int(user_input)
print (input // 1000)
print ((input % 1000) // 100)
print ((input % 100) // 10)
print ((input % 10) // 1)