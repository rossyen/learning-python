# pizza-price.py
#   A program that calculates the cost per square meter
#   of a circular pizza.


import math 

def areaPizza(radius):
    area = math.pi * (radius/2)**2
    return area

def costSquareMeterPizza(price, radius):
    costSquare = price / areaPizza(radius)
    return costSquare

def main():

# print information to user
    print('This is a program that calculates the cost per square meter of your pizza.')
    
    price =int(input('How much did you pay for your pizza in NOK? '))
    radius = int(input('How big is your pizza (in CM)? '))

    # pizzaSize = areaPizza(radius)
    costPizza = costSquareMeterPizza(price, radius)

    print(f'Your pizza costs {costPizza:.2f} kr. pr square meter.')

main()