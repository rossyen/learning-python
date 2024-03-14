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


from random import random

def printIntro():
    print("This program simulates a game of racquetball between two")
    print('players called "A" and "B". The ability of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving. Player A always")
    print("has the first serve.")

def getInputs():
    # Returns the three simulation parameters probA, probB and n
    a = 0.65 #float(input("What is the prob. player A wins a serve? "))
    b = 0.70 #float(input("What is the prob. player B wins a serve? "))
    n = 1100 #int(input("How many games to simulate? "))
    return a, b, n

def gameOver(a, b):
    return a==15 or b==15


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
    

def simNGames(n, probA, probB):
    # Simulates n games and returns winsA and winsB
    winsA = 0
    winsB = 0
    wins_requires = 3
    consecutive_winsA = 0
    consecutive_winsB = 0
    multiwinA = 0
    multiwinB = 0
    totalshutoutA = 0
    totalshutoutB = 0
    if n % 2 == 0:
        firstServe = "A"
    else:
        firstServe = "B"
    for i in range(n):
        scoreA, scoreB = simOneGame(firstServe, probA, probB)
        if scoreA == 0 or scoreB == 0:
            shutoutA, shutoutB = shutout(scoreA, scoreB)
            if shutoutA > 0:
                totalshutoutA = totalshutoutA + 1
            elif shutoutB > 0:
                totalshutoutB = totalshutoutB + 1

        if scoreA > scoreB:
            winsA = winsA + 1
            consecutive_winsA = consecutive_winsA + 1
            consecutive_winsB = 0
            if consecutive_winsA == wins_requires:
                multiwinA = multiwinA + 1
                consecutive_winsA = 0
        else:
            winsB = winsB + 1
            consecutive_winsB = consecutive_winsB + 1
            consecutive_winsA = 0
            if consecutive_winsB == wins_requires:
                multiwinB = multiwinB + 1
                consecutive_winsB = 0
    return winsA, winsB, multiwinA, multiwinB, totalshutoutA, totalshutoutB

def shutout(scoreA, scoreB):
    a = 0
    b = 0
    if scoreB == 0:
        a = a + 1 
        return a, b
    elif scoreA == 0:
        b = b + 1
        return a, b
    
def simBestOfGames(n, winsA, winsB):
    winsRequired = n/2 + 1
    if winsA >= winsRequired:
        return "A"
    elif winsB >= winsRequired:
        return "B"
    else:
        return False

def printSummary(winsA, winsB, multiWinA, multiWinB, bestOfNGames, shutoutA, shutoutB):
    # Prints a summary of wins for each player.
    n = winsA + winsB
    print(f"\nGames simulated: {n}")
    print(f"Wins for A: {winsA} ({winsA/n:0.1%})")
    print(f"Wins for B: {winsB} ({winsB/n:0.1%})\n")

    print(f'3 wins in a row for A: {multiWinA}')
    print(f'Approximately possibility for 3 wins in a row for A: {multiWinA/n:0.1%}')
    print(f'3 wins in a row for B: {multiWinB}')
    print(f'Approximately possibility for 3 wins in a row for A: {multiWinB/n:0.1%}')
    if bestOfNGames == False:
        pass
    else:
        print(f"\nPlayer {bestOfNGames} wins best of {n} games with at least {n//2+1} games won")


    print(f"\nPlayer A won a total of: {shutoutA} shutouts ({shutoutA/n:0.1%} of all games).")
    print(f"Player B won a total of: {shutoutB} shutouts ({shutoutB/n:0.1%} of all games).")


def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB, multiWinA, multiWinB, shutoutA, shutoutB = simNGames (n, probA, probB)
    bestOfNGames = simBestOfGames(n, winsA, winsB)
    
    printSummary(winsA, winsB, multiWinA, multiWinB, bestOfNGames, shutoutA, shutoutB)



if __name__ == "__main__":
    main()