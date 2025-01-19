user_input = int(input('Type first digit: '))
user_input_2 = int(input('Type second digit: '))
user_input_math = input('Type math operation (+, -, *, /): ')

if user_input_math == "+":
    result = user_input + user_input_2
    print(result)

elif user_input_math == "-":
    result = user_input - user_input_2
    print(result)

elif user_input_math == "*":
    result = user_input * user_input_2
    print(result)

elif user_input_math == "/":
    if user_input_2 == 0:
        print("Cant divide by 0")
    else:
        result = user_input / user_input_2
        print(result)