
def main():
# Print introduction
    print('This program calculates the future value')
    print('of an investment over "x" years.')

# Input the amount of the principal
    principal = int(input('Enter the initial principal: '))

# Input the annual percentage rate
    apr = float(input('Enter the annual interest rate: '))

    n = int(input('Enter how many years you want to save: '))
# Repeat 10 times:
    for i in range(n):
    # Principal = principal * (1 + apr)
        principal = principal * (1 + apr)

# Output the value of principal
    print(f'The value in {n} years is:', principal)

main()

input('Press \'enter\' key to exit program')