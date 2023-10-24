# futval-graph.py

'''
Print an introduction
Get value of principal and apr from user
Create a GraphWin
Create a 320x240 GraphWin titled ''Investment Growth Chart''
Draw scale labels on left side of window
Draw bar at position 0 with heigh corresponding to principal

For successive years 1 trough 10
    Calculate principal = principal * (1 + apr)
    Draw a bar for this year having a height corresponding to principal
Wait for user to press Enter.

'''


from graphics import *

win = GraphWin('Investment Growth Chart', 320, 240)


input()