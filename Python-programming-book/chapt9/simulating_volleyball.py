# simulating_volleyball.py

# printIntro
# getInputs
# simNGames
    # simOneGame
        # gameOver
# printSummary

from random import random

def printInto():
    print("\n")

def getInputS():
    n = 10
    probA = 0.6
    probB = 0.6

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
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
    print(f"A: {scoreA} | B: {scoreB}")
    return scoreA, scoreB

def gameOver(a, b):
    if a >= 15 or b >=15:
        if a == b + 2 or b == a + 2:
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