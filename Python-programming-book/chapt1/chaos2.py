# File: chaos2.py
# A Simple program illustrating chaotic behavior 
# This is an improvement on chaos.py

def main():

    # Welcome message
    print('This program illustrates a chaotic function on two different numbers')

    # Ask user for input on how many numbers he wants to see 
    n = eval(input('How many numbers should I print? '))

    # Ask user for input on two numbers
    x , y = (input('Enter two number between 0 and 1: ').split())
    
    # Make variables floats
    x = float(x)
    y = float(y)

    # Loop trough numbers in 'i' meaning 'ITEM' in range for 'n' which is the gives number from user
    for i in range (n):

        # Chaos formula on both x and y 
        x = 3.9 * x * (1 - x)
        y = 3.9 * y * (1 - y)

        # prints two lists with 6 decimals. 'end=('')' makes the print end without breaking the line
        print(f'{x:.6f}'.format(x),end=('   '))
        print(f'{y:.6f}'.format(y))

# Calls for main() to be run        
main()