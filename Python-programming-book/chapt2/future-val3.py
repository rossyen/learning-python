# Make a program that shows a fixed invested amount
# every year over 'x' times year

# Print welcome message
def main():
    print('This is a program that prints out invested sum and compound interest over a fixed period')
# Get input on fixed investment amount
    f_inv = int(input('How much do you want to save annually: '))

# Get interest rate
    i_rate = float(input('What interest rate do you expect: '))

# Get input on how many years to save
    n = int(input('How many years are you planning to save: '))

    amount = f_inv
# print amount saved on fixed investment over 'x' times years
    
    # loop for compound interest
    for i in range(n):
        f_inv = (f_inv * (1 + i_rate/100)) + amount
    f_sum = f_inv - amount

    # loop for value and compound interest 
    
    print(f'Earning you {f_sum} over {n} years')

main()


'''def compound_interest():
    amount = principal
    for i in range (time):
        amount = amount * (1 + rate/100)
    CI = amount - principal

    This program shows only compound interest after 'time'
'''
