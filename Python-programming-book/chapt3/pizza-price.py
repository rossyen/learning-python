# pizza-price.py
#   A program that calculates the cost per square meter
#   of a circular pizza.


import math # import math
def cost_square_meter():

# print information to user
    print('This is a program that calculates the cost per square meter of your pizza.')
    
# ask for price of pizza and store value as integer
    price_pizza =int(input('How much did you pay for your pizza in NOK? '))

# ask for size of pizza in cm and store value as integer
    size_pizza = int(input('How big is your pizza (in CM)? '))

# calculate cost per square meter
    area_pizza = math.pi * (size_pizza/2)**2
    price_area_pizza = price_pizza / area_pizza

# print result to user
    print(f'Your pizza costs {price_area_pizza:.2f} kr. pr square meter.')

cost_square_meter()