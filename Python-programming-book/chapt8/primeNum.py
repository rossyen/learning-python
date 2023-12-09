# primeNum.py

# A positive whole number n > 2 is a prim if no number between 2 and square root
# of num (inclusive) evenly divides n. Write a program that accepts a value of n
# as input and determines if the value is prime. If n it not prime,
# your program should quit as soon as it finds a value that evenly divides n.

import math

def isPrime(n):
    # special cases
    if n < 2:
        return False
    elif n == 2:
        return True
    
    # check divisibility up to the square root
    sqrt_num = math.isqrt(n) + 1
    for i in range(2, sqrt_num):
        if n % i == 0:
            return False
        
    # If no divisor found, it's a prime number
    return True

def main():
    
    n = int(input("Enter a number to see if its a prime number or not: "))

    num_to_check = n

    if isPrime(num_to_check):
        print(f'{n} is a prime number.')
    else:
        print(f'{n} is not a prime number')

if __name__ == '__main__':
    main()    