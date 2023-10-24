# guess.py


# Ask user for a value to find square root of (x)
'''
def guess():
    square_root_nr = int(input('Enter number you want to find square root of: '))
    guess =int(input('What do you think the square root is: '))

    for i in range(5):
        answer = (guess + (square_root_nr/guess)) / 2

    print (answer)

guess()'''

import math

def main():
    print("This program calculates square root using Newton's method.")
    print()

    x = float(input("Enter number to find the root of: "))
    n = int(input("How many iterations should I use? "))

    guess = x / 2.0
    for i in range(n):
        guess = (guess + x/guess)/2.0

    print()
    print("Approximate square root:", guess)
    print("Difference from math.sqrt:", math.sqrt(x) - guess)

main()