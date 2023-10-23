# distance.py
#   A program that determines the distance between two points

#   Get two points (coordinates) from input
#   store coordinates as integers
#   use math to calculate distance between points
#   print out result

import math

def distance():
    print('This is a program to calculate distance between two coordinate points')
    x1, y1 = (input('Enter starting coordinates: ').split())
    x2, y2 = (input('Enter stop coordinates: ').split())
    x1 = int(x1)
    x2 = int(x2)
    y2 = int(y2)
    y1 = int(y1)

    distance = math.sqrt((x2-x1)*2 + (y2-y1)*2)

    print(f'The distance between coordinates is {distance}')

distance()