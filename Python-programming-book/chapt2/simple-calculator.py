# This is a simple calculator to let users calculate
# with the operators:
# Addition, subtraction, multiplication, division, modulus
# Exponentiation and floor division

# Setup of program:
def simple_calculator():
# Introduction message to user
    print('This is a simple calculator that lets you use: Addition "+", subtraction "-",')
    print('multiplication "*", division "/", modulus "%", exponentiation "**" and floor division "//".')

# Loop for the program
    while True:
# Let user input two numbers and an operator which we visualize
        num1, operator, num2 = input('Please enter number followed by operator followed by number to do math: ').split()

# Store input values in floats
        num1 = int(num1)
        num2 = int(num2)
# Create a loop (100 calculations) that calculates on input operator
# Addition
        if (operator == '+'):
            print(f'{num1} {operator} {num2} equals ', num1 + num2)
            return simple_calculator()
# Subtraction
        elif (operator == '-'):
            print(f'{num1} {operator} {num2} equals ', num1 - num2)
            return simple_calculator()
# Multiplication
        elif (operator == '*'):
            print(f'{num1} {operator} {num2} equals ', num1 * num2)
            return simple_calculator()
# Division
        elif (operator == '/'):
            print(f'{num1} {operator} {num2} equals ', num1 / num2)
            return simple_calculator()
# Modulus
        elif (operator == '%'):
            print(f'{num1} {operator} {num2} equals ', num1 % num2)
            return simple_calculator()
# Exponential
        elif (operator == '**'):
            print(f'{num1} {operator} {num2} equals ', num1 ** num2)
            return simple_calculator()
# Floor division
        elif (operator == '//'):
            print(f'{num1} {operator} {num2} equals ', num1 // num2)
            return simple_calculator()

# If not integer or valid operator:
        else:
            print ('Enter an integer followed by an operator followed by an integer to do math.')

# Print result to user

# End program

simple_calculator()
