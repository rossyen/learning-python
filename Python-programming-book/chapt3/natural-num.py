# natural-num.py
#   A program that finds the sum of the first n natural numbers
#   where the value of n is provided by the user

import math

def natural_number ():
    print('This program finds the sum of the first n natural numbers.')
    print()

    natural_num = int(input('Enter a value for n: '))
    sum = 0
    for i in range(1,natural_num+1):
        sum = sum + i

    print()
    print(f'The sum from 1 to {natural_num} is {sum}')

natural_number()