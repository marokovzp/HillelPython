result = int(input('Type digit: '))
user_continue = "y"

while user_continue == "y":
    user_input_math = input('Type math operation (+, -, *, /): ')
    user_input_2 = int(input('Type next digit: '))

    if user_input_math == "+":
        result += user_input_2
        print(result)
        user_continue = input('do you want to continue (y)?: ')

    elif user_input_math == "-":
        result -= user_input_2
        print(result)
        user_continue = input('do you want to continue (y)?: ')

    elif user_input_math == "*":
        result *= user_input_2
        print(result)
        user_continue = input('do you want to continue (y)?: ')

    elif user_input_math == "/":
        if user_input_2 == 0:
            print("Cant divide by 0")
            break
        else:
            result /= user_input_2
            print(result)
            user_continue = input('do you want to continue (y)?: ')
else:
    print('end')