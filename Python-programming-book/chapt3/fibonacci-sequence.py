# fibonacci-sequence.py
#   A program that finds the 'n'th fibonacci number where
#   'n' is a value input by user.
# example: if n = 6, then the result is 8.

def fib_seq():
    print('This program lets you find the value of a number in the Fibonacci sequence.')
    print()

    n = int(input('Enter number in sequence to see value of number: '))
    a = 0
    b = 1
    for i in range(n-1):
        a,b=b,a+b

    print(b)

fib_seq()
