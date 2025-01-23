import math

user_input = input('Type digits with space: ')
list = []
for item in user_input.split():
    list.append(int(item))

user_input_math = input('Type math operation (+, -, *, /): ')

if user_input_math == "+":
    result = sum(list)
    print(result)

elif user_input_math == "-":
    result = list[0] - sum(list[1:])
    print(result)

elif user_input_math == "*":
    result = math.prod(list)
    print(result)

elif user_input_math == "/":
    result = list[0]
    for num in list[1:]:
        if num == 0:
            print("Cant divide by 0")
            break
        result /= num
    else:
        print(result)