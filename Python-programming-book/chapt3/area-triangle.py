# area-triangle.py
#   A program to calculate area of a triangle
#   given the length of its three sides


# receive input on lengths a, b and c and store in floats.
# calculate the area of triangle using Heron's formula
# print output

import math
def area_triangle():
    print('This program lets you calculate the area of a triangle when you')
    print('know the length of all sides.')
    a = float(input('Side a: '))
    b = float(input('Side b: '))
    c = float(input('Side c: '))

    s = (a+b+c)/2

    area = math.sqrt(s*(s-a)*(s-b)*(s-c))

    print(f'The area of triangle is {area:.2f}')


area_triangle()

