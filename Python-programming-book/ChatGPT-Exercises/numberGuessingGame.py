# numberGuessingGame.py

# A program that generates a random number inside a specified range
# Player must guess the number
# Game provides feedback to the player after each guess, weather number is
# too high, too low, or correct
# There is a limit to number of guesses
# Use a loop to allow the player to keep guessing until correct or limit is up

import random

# gives a random number in range from 1 to 100
def randomNumber():
    return random.randrange(101)


def main():
    print("This program lets you guess a random number in the range of 1 to 100 in 9 attempts")
    guess = int(input("Whats your guess: "))
    numberToGuess = randomNumber()
    attempts = 0

    print()

    # I've commented the 3 places you need to change, when changing number of attempts in this game.
    while True:
        attempts += 1
        
        if attempts <7: # change number here
            if guess == numberToGuess:
                print ("Correct!")
                break
            elif guess < numberToGuess:
                print ("\nThe number is to low\n")
            elif guess > numberToGuess:
                print ("\nThe number is to high\n")
            guess = int(input("Guess again: "))
        
        elif attempts == 8: # change number here
            print("\nYou have one attempt left.\n")
            guess = int(input("Guess again: "))


        elif  attempts == 9: # change number here
            print("\nYou guessed wrong and have used all your attempts. You lose.\n")
            break
        
        
if __name__ == "__main__":
    main()