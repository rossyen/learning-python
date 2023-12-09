# goldbackConjecture.py

# The Goldback conjecture asserts that every number is the sum of two prime numbers.

# Write a program that gets a number from the user, checks to make sure it is even,
# and then finds two prime numbers that add up to the number

import math

def isPrime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    sqrt_num = math.isqrt(n) + 1
    for i in range(2, sqrt_num):
        if n % i == 0:
            return False
    return True

def findPrimeForGoldback(conjecture_number):
    if conjecture_number % 2 != 0 or conjecture_number < 4:
        print("Goldbach conjecture is not applicable to this number")
        return
    for i in range(2, conjecture_number):
        if isPrime(i) and isPrime(conjecture_number - i):
            return (i), (conjecture_number - i)        
def main():

    print("To see which two prime numbers that adds up your even number, pleas enter an even number.")
    conjecture_number = int(input(": "))
    if conjecture_number % 2 != 0:
        print("Please enter an even number.")
        return
    print(f'The two prime numbers are: {findPrimeForGoldback(conjecture_number)}.')

if __name__ == '__main__':
    main()