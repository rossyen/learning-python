# Problem : Receive miles and convert to kilometers
# kilometers = miles * 1.60934
# Enter miles 5
# 5 miles equals 8.04 kilometers

# Ask the user for input miles to see how many km it is and define the input as a integer and variable
num1 = input('Enter number of miles to see how many kilometers it is: ')
num1 = int(num1)

# create variable that multiply num1 with 1.609394
kilometers = num1 * 1.60934

# print conversion of miles to km to user
print('{} miles equals to {} kilometers'.format(num1,kilometers))