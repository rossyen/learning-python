# windChill_Index.py

# prints a table of windchill values
# Formula only works if wind speed is in excess of 3 mph

# Formula:
# 35.74 + 0.6215*T - 35.75(V**0.16) + 0.4275(V**0.16)
# T = temperature in Fahrenheit, and V is the wind speed in miles per hour

# We want to print out a nicely formatted table of windchill values.
# Rows should represent:
# Side colum: wind speed from 0 to 50 in 5-mph increments
# Top colum: temperature in fahrenheit from -20 to 60 in 10 degree increments

''' 

Note to self:
Program prints ok if you have file graphics.py in same directory
Next problem to solve is to correct the formula to show correct windChill values.
At the moment the program formats neatly in a popup window, but the numbers are incorrect.



'''
import math

def windChillFormula(T, V):
    windChill = 35.74 + 0.6215*T - 35.75*(V**0.16) + 0.4275*T*(V**0.16)
    windChill = math.ceil(windChill)
    windChill = int(windChill)
    return windChill

from graphics import *
def main():

    win = GraphWin("WindChill Index", 720, 500)
    win.setBackground("white")

# top colum for temperature from - 20 to + 60 degrees
    temp = -30
    tempLoop = 0
    for i in range(11):
        tempLoop = tempLoop + 50
        temp = temp + 10
        Text(Point(tempLoop+40, 55), f'{temp:>2}').draw(win)

# left colum  for wind in mph from 0 to 50 in 5 increments
    wind = 0
    windLoop = 0
    for i in range(10):
        windLoop = windLoop + 35
        wind = wind + 5
        Text(Point(20, windLoop+50), f'{wind:>2}').draw(win)

# loop trough and print windchill temp for each colum from left to right
    # test loop with  temp + wind

    tempList =[-20, -10, 0, 10, 20, 30, 40, 50, 60, 70, 80]
    windList =[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

    # first windchill line
    windChillLoop1 = 0 
    increasePoint = 0
    for i in range(11):
        windChill = windChillFormula (tempList[i], windList[0])
        windChillLoop1 = windChillLoop1 + 50
        Text(Point(windChillLoop1+40, increasePoint+85), f'{windChill:>2}').draw(win)

    # 2line
    windChillLoop2 = 0 
    increasePoint = 35 
    for i in range(11):
        windChill = windChillFormula (tempList[i], windList[1])
        windChillLoop2 = windChillLoop2 + 50
        Text(Point(windChillLoop2+40, increasePoint+85), f'{windChill:>2}').draw(win)
    # 3rd line
    windChillLoop3 = 0 
    increasePoint = 35*2
    for i in range(11):
        windChill = windChillFormula (tempList[i], windList[2])
        windChillLoop3 = windChillLoop3 + 50
        Text(Point(windChillLoop3+40, increasePoint+85), f'{windChill:>2}').draw(win)
    # 4th
    windChillLoop3 = 0 
    increasePoint = 35*3
    for i in range(11):
        windChill = windChillFormula (tempList[i], windList[3])
        windChillLoop3 = windChillLoop3 + 50
        Text(Point(windChillLoop3+40, increasePoint+85), f'{windChill:>2}').draw(win)
    # 5th
    windChillLoop3 = 0 
    increasePoint = 35*4
    for i in range(11):
        windChill = windChillFormula (tempList[i], windList[4])
        windChillLoop3 = windChillLoop3 + 50
        Text(Point(windChillLoop3+40, increasePoint+85), f'{windChill:>2}').draw(win)
   
    # 6th
    windChillLoop3 = 0 
    increasePoint = 35*5
    for i in range(11):
        windChill = windChillFormula (tempList[i], windList[5])
        windChillLoop3 = windChillLoop3 + 50
        Text(Point(windChillLoop3+40, increasePoint+85), f'{windChill:>2}').draw(win)
   
    # 7th
    windChillLoop3 = 0 
    increasePoint = 35*6
    for i in range(11):
        windChill = windChillFormula (tempList[i], windList[6])
        windChillLoop3 = windChillLoop3 + 50
        Text(Point(windChillLoop3+40, increasePoint+85), f'{windChill:>2}').draw(win)
   
    # 8th
    windChillLoop3 = 0 
    increasePoint = 35*7
    for i in range(11):
        windChill = windChillFormula (tempList[i], windList[7])
        windChillLoop3 = windChillLoop3 + 50
        Text(Point(windChillLoop3+40, increasePoint+85), f'{windChill:>2}').draw(win)
    
    # 9th
    windChillLoop3 = 0 
    increasePoint = 35*8
    for i in range(11):
        windChill = windChillFormula (tempList[i], windList[8])
        windChillLoop3 = windChillLoop3 + 50
        Text(Point(windChillLoop3+40, increasePoint+85), f'{windChill:>2}').draw(win)
   
    # 10th
    windChillLoop3 = 0 
    increasePoint = 35*9
    for i in range(11):
        windChill = windChillFormula (tempList[i], windList[9])
        windChillLoop3 = windChillLoop3 + 50
        Text(Point(windChillLoop3+40, increasePoint+85), f'{windChill:>2}').draw(win)

# Information text in program
    Text(Point(300, 15),"WindChill Index").draw(win) # Top text
    Text(Point(30, 35),"Wind").draw(win) # wind mph text
    Text(Point(30, 55),"(mph)").draw(win) # wind mph text
    Text(Point(300, 35),"Temperature (Fahrenheit)").draw(win) # temp C text


    input("Press <Enter> to quit")
    win.clos()
main()