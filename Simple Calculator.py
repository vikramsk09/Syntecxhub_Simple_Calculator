import math

while True:
    exit = input("\nPress 'e' to exit or 'enter' to continue: ")

    if exit == "e":
        break

    else:
        num1 = input("Enter the first number: ")
        operator = input("Enter the operation you wish to perform (+,-,*,/): ")

        num2 = input("Enter the second number: ")

        num1 = float(num1)
        num2 = float(num2)

        if operator == "+":
            result = num1 + num2

        elif operator == "-":
            result = num1 - num2

        elif operator == "*":
            result = round(num1 * num2, 2)

        elif operator == "/":
            if num2 == 0:
                print("Error! Divide by zero not possible.")
            else:
                result = round(num1/num2, 2)

        else:
            print("Invalid operator entered")

        try:
            print(num1, operator, num2, "=", result)
        except NameError as e:
            print(e)
