# maxn.py
# Determine which of three user inputs is the largest
# This program can be completed with the us of "max" python
# function instead of all the code entered.

def main():
    n = int(input("How many numbers are there? "))
    
    # Set max to be the first value

    maxval = float(input("Enter a number >> "))

    # Compare the n-1 successive values
    for i in range(n-1):
        x = float(input("Enter a number >> "))
        if x > maxval:
            maxval = x
        
    print(f"The largest value is {maxval}")


if __name__ == '__main__':
    main()
