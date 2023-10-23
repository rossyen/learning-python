# date-of-easter.py
#   A program to figure out the date of Easter

# Date is calculated by these formulas (using int arithmetic):
# C = year//100 
# epact = (8 + (C//4)- C + ((8*C + 13)//25) + 11(year%19))%30 

# Ask user for a 4-digit year
# calculate value of epact
# output value of epact

def date_of_easter():
    year = int(input('Enter a 4-digit year to see the Gregorian epact value of year: '))
    c = year // 100
    epact = (8+(c//4) - c + ((8*c + 13)//25) + 11 * (year % 19)) %30

    print(f'The epact value is {epact} days.')

date_of_easter()