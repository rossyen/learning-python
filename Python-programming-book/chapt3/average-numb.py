# average-number.py
#   A program that averages a series of numbers entered by the user.
#   Ask user for how many numbers are to be averaged
#   Ask user for each of the numbers in turn and print out a total sum
#   after all the numbers have been entered


def averages_of_numbers():
    print('This program lets you see the average of numbers entered, and you choose which, and how many numbers are entered.')
    print()

    n = int(input('How many numbers do you want to average out of : '))
    sum_average = 0
    for i in range(n):
        sum_numbers = int(input('Enter number: '))
        sum_average = sum_average + sum_numbers


    print(f'The average of your numbers are: {sum_average / n}')


averages_of_numbers()
