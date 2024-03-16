# simulating_Volleyball_rally_scoring.py

'''
Most sanctioned volleyball is now played using rally scoring. '
In this system, the team that wins a rally is awarded a point, even if they were not the serving team. 
Games are played to a score of 25. Design and implement a simulation of volleyball using rally scoring. 
'''

from random import random

def printInto():
    print("\n")

def getInputS():
    n = 1
    probA = 0.65
    probB = 0.65

    return probA, probB, n

def simNGames(n, probA, probB):
    winsA = 0
    winsB = 0
    if n % 2 == 0:
        firstServe = "A"
    else:
        firstServe = "B"
    for i in range(n):
        scoreA, scoreB = simOneGame(firstServe, probA, probB)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB

    
def simOneGame(firstServe, probA, probB):
    scoreA = 0
    scoreB = 0
    serving = firstServe
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
                scoreB = scoreB + 1
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
                scoreA = scoreA + 1
    return scoreA, scoreB

def gameOver(a, b):
    if a >= 25 or b >=25:
        if a == b + 1 or b == a + 1:
            return False
        elif a == b:
            return False
        else: 
            return True


def printSummary(winsA, winsB):
    n = winsA + winsB
    print(f"\nGames simulated: {n}")
    print(f"Wins for A: {winsA} ({winsA/n:0.1%})")
    print(f"Wins for B: {winsB} ({winsB/n:0.1%})\n")

def main():
    printInto()
    probA, probB, n = getInputS()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)


if __name__ == "__main__":
    main()