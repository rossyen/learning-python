# Make a program that shows a fixed invested amount
# every year over 'x' times year

# Print welcome message
def main():
    print('This is a program that prints out invested sum with contributing saving and compound interest over a fixed period')
# Get input on starting amount on savings
    principal = int(input('Enter initial savings: '))
    
# Get interest rate
    rate = float(input('What interest rate do you expect: '))

# Get input on how many years to save
    t = int(input('How many years are you planning to save: '))

    n = 1 # Determines compounding frequency in formula

# Get input on contributing saving fro user:
    contributing = int(input('How much would you like to save each year? '))


# print amount saved on fixed investment over 'x' times years
    
    A = (principal * (1 + rate/n)**(n*t)) + (contributing * (((1 + rate/n)**(n*t)) -1) / (rate/n))
        
    print(f'Earning you {A:.2f} over {t} years')

main()


'''def compound_interest():
    amount = principal
    for i in range (time):
        amount = amount * (1 + rate/100)
    CI = amount - principal

    This program shows only compound interest after 'time'
'''


''' 
Definitions: 
A= is the final value of the account after interest is calculated
P= principal 
r= annual interest rate
n= compounding frequency
t= time period in years
PMT= 'PMT stands for payment' and in the formula it is the contributions place

Compound interest formula:

A = P * (1 + r/n)**(n*t)

Compound interest with regular contributions: Note this formula only
works if the payment frequency and compounding frequency are the same.
For example, if you make monthly contributions, and the interest compounds
quarterly, this formula will not be accurate. 

A = (P * (1 + r/n)**(n*t)) + ((PMT * ((1 + r/n)**(n*t) -1)) / (r/n))

'''
