
def main():
# Print introduction
    print('This program calculates the future value')
    print('of a 10-year investment.')

# Input the amount of the principal
    principal = int(input('Enter the initial principal: '))

# Input the annual percentage rate
    apr = float(input('Enter the annual interest rate: '))

# Repeat 10 times:
    for i in range(10):
    # Principal = principal * (1 + apr)
        principal = principal * (1 + apr)

# Output the value of principal
    print('The value in 10 years is:', principal)

main()