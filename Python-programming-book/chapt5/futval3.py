# futval3.py
# improved version of futval.py program from chapt 2.

def main():
# Prompt user for amount to invest
    principal = 2000 #int(input("Initial principal: "))
# Prompt user for annualized interest rate
    apr = 0.1 #float(input("Enter the annualized interest rate: "))
# Prompt user for how many years to invest
    years = 7 #int(input("Enter number of years: "))

# loop trough the invested amount times interest rate and how many years
    print("Year\t  Value")
    print("----------------")
    for i in range(years + 1):
        print("{0:3}{1:12.2f}".format(i, principal))
        principal = principal * (1 + apr)
# print output neatly to user

        
main()