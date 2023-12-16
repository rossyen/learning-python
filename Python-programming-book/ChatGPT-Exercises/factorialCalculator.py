# factorialCalculator.py

# a program that calculates the factorial of a given non-negative integer.
import math
try:
    x = int(input("Enter a number to see factorial (x!): "))
    print(f"The factorial of {x} is {math.factorial(x)}")
except ValueError:
    print("Enter a positive number to see the factorial.")