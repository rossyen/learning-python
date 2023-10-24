# ladder-height.py
#   A program that determines the length of a ladder to reach a given
#   hight when leaned against the house.
#   The heigh and angle of the ladder are given as inputs

import math

def ladder_height():
    height = float(input('Enter height of ladder: '))
    angle = float(input('Enter angle of ladder: '))

    length = height / math.sin(angle)

    print(f'The required length of ladder is {length:.2f}')

ladder_height()