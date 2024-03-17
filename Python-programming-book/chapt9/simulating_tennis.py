# simulating_tennis.py

# Exercise:
'''
Design and implement a simulation of some other racquet sport (e.g., tennis or table tennis). 
'''

# printInto
# getInputs
# simNgames
    # best of 5 sets
# serve/Service
    # 2 serves per point
# gameOver
    # advantage and duce
# printSummary

from random import randrange, random

def printIntro():
    print("This is a simulation of the probability a player wins best of 5 game of tennis.")
    print("You will need to add the chance that player A and player B has to wins a serve.\n")

def getInputs():
    n = 5
    probA = float(input("What is the chance player A wins a serve? "))
    probB = float(input("What is the chance player B wins a serve? \n"))
    return probA, probB, n

def simNgames(n, probA, probB):
    setsA = 0
    setsB = 0
    firstServe = randrange(0,2) # coin toss who starts
    while not simBestOfGames(n, setsA, setsB):
        scoreA, scoreB = simOneGame(firstServe, probA, probB)
        if scoreA > scoreB:
            setsA += 1
        else:
            setsB += 1
    print(f"Sets won A: {setsA} | Sets won B:{setsB}")
    return setsA, setsB

def simOneGame(firstServe, probA, probB):
    scoreA = 0
    scoreB = 0
    serving = firstServe
    while not gameOver(scoreA, scoreB):
        if serving == 1:
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = 0
                scoreB += 1
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = 1
                scoreA += 1
    return scoreA, scoreB

def gameOver(a, b):
    if a >= 4 or b >= 4:
        if a == b + 1 or b == a + 1:
            return False
        elif a == b:
            return False
        else: 
            return True
        
def simBestOfGames(n, setsA, setsB):
    winsRequired = n/2 + 1
    if setsA >= winsRequired:
        return True
    elif setsB >= winsRequired:
        return True
    else:
        return False
    
def printSummary(setA, setsB):
    if setA > setsB:
        print(f"Player A wins the game!")
    else:
        print(f"Player B wins the game!")

def main():
    printIntro()
    probA, probB, n = getInputs()
    setsA, setsB = simNgames(n, probA, probB)
    printSummary(setsA, setsB)

if __name__ == "__main__":
    main()