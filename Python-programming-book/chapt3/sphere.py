# sphere.py
#   A program that calculates the volume and surface area
#   of a sphere from its radius, given as input

import math

def volume_area_sphere():

#   Print a welcoming message to user
    print('This is a program that shows you both the volume and area of a sphere')

#   Get input from user on radius on sphere
    radius = int(input('Please enter the radius of you sphere to see volume and surface: '))

#   Calculate volume
    volume = 4 / 3 * math.pi * radius**3

#   Calculate area
    area = 4 * math.pi * radius**2

#   Print results
    print(f'The volume is {volume:.2f} and the area is {area:.2f} for a sphere with radius of {radius}.')

volume_area_sphere()

