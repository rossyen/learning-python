# simulating_racquetball.py

# Notes:
'''
All inputs are assumed to be legal numerical values; no error or validity
checking is required.

In each game, player A serves first.
'''

# Input
'''
The program first prompts for and gets the service probabilities of the two players
(called "player A" and "player B"). Then the program prompts
for and gets the number og games to be simulated
'''

# Output
'''
The program will provide a series of initial prompts such as the following:

What is the prob. player A wins a serve?
What is the prob. player B wins a serve?
How many games to simulate?


The program will print out a nicely formatted report showing the number
of games simulated and the number of wins and winning percentage for each player.
Here is an example:

Games Simulated: 500
Wins for A: 268 (53.6%)
Wins for B: 232 (46.4%)
''' 


# top-down design:

# Print an Introduction
# Get the inputs: probA, probB, n
# Simulate n games of racquetball using probA and probB
# Print a report on the wins for playerA and playerB

from random import random

def printIntro():
    print("This program simulates a game of racquetball between two")
    print('players called "A" and "B". The ability of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving. Player A always")
    print("has the first serve.")

def getInputs():
    # Returns the three simulation parameters probA, probB and n
    a = float(input("What is the prob. player A wins a serve? "))
    b = float(input("What is the prob. player B wins a serve? "))
    n = int(input("How many games to simulate? "))
    return a, b, n

def gameOver(a, b):
    return a==15 or b==15


def simOneGame(probA, probB):
    scoreA = 0
    scoreB = 0
    serving = "A"
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
    
    return scoreA, scoreB
    

def simNGames(n, probA, probB):
    # Simulates n games and returns winsA and winsB
    winsA = 0
    winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB

def printSummary(winsA, winsB):
    # Prints a summary of wins for each player.
    n = winsA + winsB
    print(f"\nGames simulated: {n}")
    print(f"Wins for A: {winsA} ({winsA/n:0.1%})")
    print(f"Wins for B: {winsB} ({winsB/n:0.1%})")
    

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames (n, probA, probB)
    printSummary(winsA, winsB)



if __name__ == "__main__":
    main()