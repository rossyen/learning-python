# number-series.py
#   A program that sum a series of numbers entered by the user.
#   Ask user for how many numbers are to be summed
#   Ask user for each of the numbers in turn and print out a total sum
#   after all the numbers have been entered


def sum_of_numbers():
    print('This program lets you see the sum of numbers entered, and you choose which, and how many numbers are entered.')
    print()

    n = int(input('How many numbers do you want to sum: '))

    for i in range(n):
        sum_numbers = int(input('Enter number: '))
        sum_numbers = sum_numbers + sum_numbers

    print(f'The sum of your numbers is {sum_numbers}')


sum_of_numbers()
