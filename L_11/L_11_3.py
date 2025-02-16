def is_even(number):
    string = str(number)
    last = int(string[len(string)-1])
    for i in (range(0, 10, 2)):
        if i == last:
            return True
    return False


assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print('Ok')