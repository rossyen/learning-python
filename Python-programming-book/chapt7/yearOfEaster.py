# yearOfEaster.py
# Computes the date of easter in the years 1982-2048

# Formula to get the date of easter:
# a = year % 19
# b = year % 4
# c = year & 7
# d = (19a + 24) % 30
# e = (2b + 4c + 6d + 5) % 7
# Date of Easter is March 22 + d + e (Date can be in april)

# Receive year from user
# determine if year is in range of 1982-2048
# Use formula in code to calculate date
# determine if date is in march or april
# print result to user

def loop():
    loop = input('Type "y" to try again, else press enter to exit\n')
    print()
    if loop == ('y'):
        return main()
    else:
        exit

def main():

    try:
        print("This program lets you see the date of Easter in the years between 1982-2048\n")
        year = int(input("Which year would you like to see the date of Easter? "))
        a = year % 19
        b = year % 4
        c = year % 7
        d = (19*a + 24) % 30
        e = (2*b + 4*c + 6*d + 5) % 7
        easter = 22 + d + e
        
        if year < 1982:
            print("Please enter a year between 1982 and 2048.")
        elif year > 2048:
            print("Please enter a year between 1982 and 2048.")
        else:
            if easter <= 31:
                print(f"The date of easter is March {easter} in the year {year}")
            elif easter > 31:
                easter = easter - 31
                print(f"The date of easter is April {easter} in the year {year}")
            else:
                print("Neat")       
    except ValueError:
        print("Please enter a year between the year 1982 and 2048")


    loop()  

if __name__ == '__main__':
    main()