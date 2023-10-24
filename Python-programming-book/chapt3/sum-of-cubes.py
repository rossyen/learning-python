# sum-of-cubes.py
#   A program that finds the sum of the cubes of the first n natural
#   numbers where the value of n is provided by the user


def sum_of_cubes():
    print('This program shows the sum of cubes of the first n natural numbers.')
    print()

    n1 = int(input('Enter first number: '))
    n2 = int(input('Enter second number: '))

    sum_cubes = n1**3 + n2**3

    print(f'The sum of cubes is {sum_cubes}')

sum_of_cubes()