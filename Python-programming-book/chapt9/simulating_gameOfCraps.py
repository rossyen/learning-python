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
    print("This is a program that simulates multiple games of craps and estimates \nthe probability that the player wins.\n")
    print("If initial roll is 2, 3 or 12 the player loses. If initial roll is 7 or 11, the player wins")
    print("Any other roll causes the player to re-roll until either rolling a 7 for lose, or re-rolling initial roll for win!\n")
    print(f"Games simulated: {gamesSimulates}\n")

    return gamesSimulates

def simulateOneGame():
    dice1 = randint(1,6)
    dice2 = randint(1,6)
    # print(f"Initial dice: {dice1 + dice2}") | testcode
    win = 0
    lose = 0
    if initialRoll(dice1, dice2) == "WIN":
        win += 1
    elif initialRoll(dice1, dice2) == "LOSE":
        lose += 1
    else:
        re_roll = gameOver(dice1, dice1)
        if re_roll == "WIN":
            win += 1
        else:
            lose += 1
    return win, lose

def simulateNgames(n):
    wins = 0
    loses = 0
    for i in range(n):
        win, lose = simulateOneGame()
        if win > lose:
            wins += 1
        else:
            loses +=1
    return wins, loses

def initialRoll(dice1, dice2):
    wins = [7, 11]
    loses = [2, 3, 12]
    for i in wins:
        if (dice1 + dice2) == i:
            return "WIN"
    for i in loses:
        if (dice1 + dice2) == i:
            return "LOSE"

def gameOver(dice1, dice2):
    initialRoll = dice1 + dice2
    newDice1 = randint(1,6)
    newDice2 = randint(1,6)
    # print(f"New dice: {newDice1 + newDice2}") testcode
    if newDice1 + newDice2 == initialRoll:
        return "WIN"
    elif newDice1 + newDice2 == 7:
        return "LOSE"
    else:
        gameOver(newDice1, newDice2)

def printSummary(wins, loses):
    print(f"\nPlayer wins: {wins}")
    print(f"Player loses: {loses}")
    print(f"The estimated probability of winning crabs is: {wins/loses:0.1%}")

def main():
    n = printIntro()
    wins, loses = simulateNgames(n)
    printSummary(wins, loses)

if __name__ == "__main__":
    main()
