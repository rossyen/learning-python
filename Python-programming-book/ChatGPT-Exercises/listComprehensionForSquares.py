# listComprehensionForSquares.py

# a program that generates a list of squares for the number in a given range.

import math

def squares(n1, n2):
    # List comprehension (creates a new list based on the values of an existing list)
    return[i**2 for i in range (n1, n2 +1)]

def main():
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    print(f"The squares in range from {n1} to {n2} are {squares(n1, n2)}")

if __name__ == "__main__":
    main()
