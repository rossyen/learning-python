# Case 4:
# Have the user enter their investment amount and their expected interest
# Each year their investment will increase by their investment + their investment + interest rate
# Print out the earning after a 10 year period

# Note to self: Did not complete this without looking at solution in video

# Ask user to enter investment amount and their expected interest

investment, interest = input('Enter investment sum and expected interest rate to see earning after 10 years: ').split()

# convert value to float
investment = float(investment)

# convert value to a float and round the percentage rate by 2 digits
interest = float(interest) * .01 # the * .01 at the end rounds the percentage by 2 digits. 

# Cycle trough 10 years using a for loop and range from 0 to 9
for i in range (10): # i cycled wrong by using (0,9) and got 9 years of investment
    investment = investment + (investment * interest) # i had wrong formula at de start

# Print out earning after a 10 year period
print('Investment after 10 years: {:.2f}'.format(investment))

