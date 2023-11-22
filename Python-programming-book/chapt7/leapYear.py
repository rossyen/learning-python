# leapYear.py
# A program to determine whether a year is a leap year.

# Receive input on year
# test if century
# if century divide by 400
# leap year
# else not leap year

# if not century
# test year and divide by 4
# if leap year print output
# if not leap year print output

def loop():
    loop = input('Type "y" to try again, else press enter to exit\n')
    print()
    if loop == ('y'):
        return main()
    else:
        exit

def isCentury(year):
    if year % 100 == 0:
        return True
    else:
        return False
    
def isDivisible400(year):
    if year % 400 == 0:
        return True
    else:
        return False
    
def isDivisible4(year):
    if year % 4 == 0:
        return True
    else:
        return False

def main():

    try:
        
        print("This program lets you see if a year is a leap year or not.\n")

        year = int(input("Enter the year to receive info if leap year or not: "))

        if isCentury(year) == True:
            if isDivisible400(year) == True:
                print(f"{year} is a leap year")
            else: print(f"{year} is not a leap year")
        elif isDivisible4(year) == True:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")


    except ValueError:
        print("Enter year to see if it is a leap year or not.")

    loop()  

if __name__ == '__main__':
    main()