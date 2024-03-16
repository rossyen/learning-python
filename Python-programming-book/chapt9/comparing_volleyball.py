# comparing_volleyball.py

'''
Design and implement a system that compares regular volleyball games
to those using rally scoring. Your program should be able to investigate
whether rally scoring magnifies, reduces, or has no effect on the relative
advantage enjoyed by the better team. 
'''

# This program tests the score in both regular volleyball games and using rally score
# Comparing the two score types we can see that the better player wins more matches
# with standard score, and the worse player wins more matches when playing
# with rally score. Thus rally score should be played for overall enjoyment.

from random import random

def printInto():
    print("\n")

def getInputS():
    n = 1000
    probA = 0.7
    probB = 0.5

    return probA, probB, n

def simNGames(n, probA, probB):
    #win for rally score
    winsA = 0
    winsB = 0
    #wins for standard score
    wins_A = 0
    wins_B = 0
    if n % 2 == 0:
        firstServe = "A"
    else:
        firstServe = "B"
    
    for i in range(n):
        scoreA, scoreB = simOneGameRallyScore(firstServe, probA, probB)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1

    for i in range(n):
        scoreA, scoreB = simOneGame(firstServe, probA, probB)
        if scoreA > scoreB:
            wins_A = wins_A + 1
        else:
            wins_B = wins_B + 1
    return winsA, winsB, wins_A, wins_B

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
    return scoreA, scoreB
    
def simOneGameRallyScore(firstServe, probA, probB):
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

def gameOverRallyScore(a, b):
    if a >= 25 or b >=25:
        if a == b + 1 or b == a + 1:
            return False
        elif a == b:
            return False
        else: 
            return True
        
def gameOver(a, b):
    if a >= 15 or b >=15:
        if a == b + 1 or b == a + 1:
            return False
        elif a == b:
            return False
        else: 
            return True


def printSummary(winsA, winsB, wins_A, wins_B):
    n = winsA + winsB
    print(f"\nGames simulated: {n}")

    print("Wins for rally score volleyball:")
    print(f"Wins for A: {winsA} ({winsA/n:0.1%})")
    print(f"Wins for B: {winsB} ({winsB/n:0.1%})\n")

    
    print("Wins for standard score volleyball:")
    print(f"Wins for A: {wins_A} ({wins_A/n:0.1%})")
    print(f"Wins for B: {wins_B} ({wins_B/n:0.1%})\n")

    print(f"Difference in wins for games: \n")
    print(f"Statistically the better player wins approximately {(wins_A-winsA)/n:0.1%} more matches")
    print(f"when playing with standard score.\n")
    print(f"And the worse player wins approximately {(winsB-wins_B)/n:0.1%} less matches")
    print(f"when playing with rally score.\n")


def main():

    printInto()
    probA, probB, n = getInputS()
    winsA, winsB, wins_A, wins_B = simNGames(n, probA, probB)
    printSummary(winsA, winsB, wins_A, wins_B)


if __name__ == "__main__":
    main()
