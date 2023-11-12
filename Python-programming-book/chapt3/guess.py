# guess.py
# Ask user for a value to find square root of (x)
import math

def nextGuess(guess, x):
    return (guess + x/guess)/2.0

def squareRoot(x, iters):
    guess = x / 2.0
    for i in range(iters):
         guess = nextGuess(guess,x)
    return guess

def main():
    print("This program calculates square root using Newton's method.")
    print()

    x = float(input("Enter number to find the root of: "))
    n = int(input("How many iterations should I use? "))

    print()
    print(f"The square root is {squareRoot(x, n)}")
main()