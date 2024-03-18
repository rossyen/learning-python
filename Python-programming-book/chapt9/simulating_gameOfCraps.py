# simulating_gameOfCraps.py

# Exercise:
'''
Craps is a dice game played at many casinos. A player rolls a pair of normal
six-sided dice. If the initial roll is 2, 3, or 12, the player loses. If the roll is
7 or 11, the player wins. Any other initial roll causes the player to "roll for
point." That is, the player keeps rolling the dice until either rolling a 7 or
re-rolling the value of the initial roll. If the player re-rolls the initial value
before rolling a 7, it's a win. Rolling a 7 first is a loss.

Write a program to simulate multiple games of craps and estimate the
probability that the player wins. For example, if the player wins 249 out of
500 games, then the estimated probability of winning is 249/500 = 0.498.
'''

# printIntro
# simulateNGames
# simulateOneGame
# initialRoll
# gameOver
# initialRoll
# printSummary

from random import randint

def printIntro():
    gamesSimulates = 1000
    print("This is a program that simulates multiple games of craps and estimates \nthe probability that the player wins.")
    print(f"Games simulated: {gamesSimulates}\n")

    return gamesSimulates

def simulateOneGame():
    dice1 = randint(1,6)
    dice2 = randint(1,6)
    win = 0
    lose = 0
    if initialRoll(dice1, dice2):
        win += 1
    elif initialRoll(dice1, dice2) == False:
        lose += 1
    else:
        while not gameOver():
            if gameOver() == True:
                win += 1
            elif gameOver() == False:
                lose += 1
            else:
                pass
    return win, lose


def initialRoll(dice1, dice2):
    wins = [2, 3, 12]
    loses = [7, 11]
    for i in wins:
        if dice1 + dice2 == i:
            return True
    for i in loses:
        if dice1 + dice2 == i:
            return False
    return None

def gameOver(dice1, dice2):
    initialRoll = dice1 + dice2
    newDice1 = randint(1,6)
    newDice2 = randint(1,6)
    if newDice1 + newDice2 == initialRoll:
        return True
    elif newDice1 + newDice2 == 7:
        return False


def main():
    n = printIntro()
    wins, loses = simulateOneGame()

if __name__ == "__main__":
    main()
