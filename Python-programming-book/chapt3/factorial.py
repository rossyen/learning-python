# factorial.py
#   A program that will compute the factorial of a
#   number entered by the user

# Input number to take factorial of, n
# Compute factorial of n, fact
# Output fact

# Initialize the accumulator variable
# Loop until final result is reached
#   Update the value of accumulator variable

def main ():
    n = int(input('Please enter a whole number: '))
    fact = 1
    for factor in range(n,1,-1):
        fact = fact * factor
    print('The factorial of', n, 'is', fact)

main()