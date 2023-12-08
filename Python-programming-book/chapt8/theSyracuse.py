# theSyracuse.py

# This program prints the Syracuse sequence from user input

# get input from user
# def syracuse
# if x is even num syr(x)=x/2
# if x is odd syr(X)=3x+1
# print result

def syracuse(x):
    sequence = [x]
    while x != 1:
        if x % 2 == 0:
            x = x//2
        else:
            x = 3*x+1
        sequence.append(x)
    return sequence
    
def main():

    print("This program lets you see the Syracuse sequence from a number of your choosing.\n")

    userNumber = int(input("Enter a number: "))
    sequence = syracuse(userNumber)

    print(f"The Syracuse sequence for your number \n{sequence} ")

main()