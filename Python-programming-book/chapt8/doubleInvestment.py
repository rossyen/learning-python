# doubleInvestment.py

# A program that uses a while loop to determine how long it takes
# for an investment to double at a given interest rate.
# Input will be an annualized interest rate, and output is the number
# of years it takes an investment to double



# Get input from user on interest rate
# use while loop to loop add interest rate until double
# print how many years it takes to double


def main():
    try:
        interestRate = float(input("Enter interest rate for your investment: "))
        interestRate = interestRate/100
        investment = 1
        years = 0

        while investment < 2:
            investment = investment * (1 + interestRate)
            years = years + 1
    
    
        print (f"It takes {years} years to double investment at {interestRate*100}% interest rate.")

    except ValueError:
        print("Enter your interest rate in format 0 to 100 (percentage %)")

main()
