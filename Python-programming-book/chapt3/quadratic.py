# quadratic.py
#   A program that computes the real roots of a quadratic equation.
#   Illustrates use of the math library.
#   Note: This program crashed if the equation has no real roots.

import math # Makes the math library available.

def quadratic(a, b, c):
    discrim = b * b - 4 * a * c
    if discrim < 0:
        print("\nThe equation har no real roots!")
    else:
        discRoot = math.sqrt(b * b - 4 * a * c)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        print(f"\nThe solutions are: {root1}, {root2}")

def main():
    print('This program finds the real solutions to a quadratic')
    print()

    a = float(input('Enter coefficient a: '))
    b = float(input('Enter coefficient b: '))
    c = float(input('Enter coefficient c: '))
    quadratic(a, b, c)    

if __name__ == '__main__':
    main()