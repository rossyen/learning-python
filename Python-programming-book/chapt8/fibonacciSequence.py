# fibonacciSequence.py

# Each number in the sequence (after the first two) is the sum of the previous two.

# This program computes and outputs the 'n'th Fibonacci number, where 'n' is
# a value entered by the user.


def fibonacciSequence(n):
    a = 0
    b = 1
    for i in range (n-1):
        a,b=b,a+b
    return b

def main():
    print('This program lets you find the value of a number in the Fibonacci sequence.')
    print()

    n = int(input('Enter number in sequence to see value of number: '))
    print(fibonacciSequence(n))

if __name__ == '__main__':
    main()
