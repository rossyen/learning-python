# sphere.py
#   A program that calculates the volume and surface area
#   of a sphere from its radius, given as input

import math

def sphereArea(radius):
    area = 4 * math.pi * radius**2
    return area

def sphereVolume(radius):
    volume = 4 / 3 * math.pi * radius**3
    return volume

def main():

    print('This is a program that shows you both the volume and area of a sphere')

    radius = int(input('Please enter the radius of you sphere to see volume and surface: '))

    area = sphereArea(radius)
    volume = sphereVolume(radius)

    print(f'The volume is {volume:.2f} and the area is {area:.2f} for a sphere with radius of {radius}.')

main()