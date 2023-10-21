# change.py
#   A program to calculate the value of som change in dollars

def main():
    print('Change counter')
    print()
    print('Please enter the count of each coin type.')
    quarters = int(input('Quarters: '))
    dimes = int(input('Dimes: '))
    nickles = int(input('Nickles: '))
    pennies = int(input('Pennies: '))
    total = quarters * .25 + dimes * .10 + nickles * .05 + pennies * .01
    print()
    print('The total value of your change is', total)

main()
