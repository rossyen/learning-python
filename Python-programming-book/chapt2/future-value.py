# Example program to see future value of a sum with interest over 10 year period

# Print introduction
def main():
    print('Hello, do you want to see how much you can earn after 10 years saving?')
# Ask for investment sum
    inv_sum = int(input('If so enter the sum you would like to save for 10 years: '))
# Ask for interest rate
    int_rate = int(input('What interest rate do you get on saving?: '))
# Store investment sum and interest rate as integers

# Use a for loop to go trough 10 years investment and calculate 
    for i in range (10):
        inv_sum = inv_sum + (inv_sum * (int_rate * .01)) 
    print (f'After 10 years your saving will become: {inv_sum:.2f}')
# Print value after 10 years

main()