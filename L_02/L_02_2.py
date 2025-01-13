user_input = input('Type 5 digits: ')
print('reverted number is:')

digits = int(user_input)
d1 = (digits // 10000)
d2 = ((digits % 10000) // 1000) * 10
d3 = ((digits % 1000) // 100) * 100
d4 = ((digits % 100) // 10) * 1000
d5 = ((digits % 10) // 1) * 10000

print (d1 + d2 + d3 + d4 + d5)
