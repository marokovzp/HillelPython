user_input = input('Type 4 digits: ')
print('You inputed next digits:')

digits = int(user_input)
print(digits // 1000)
print((digits % 1000) // 100)
print((digits % 100) // 10)
print((digits % 10) // 1)