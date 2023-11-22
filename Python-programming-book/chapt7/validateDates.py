# validateDates.py



# accept date in format dd/mm/yyyy
# validate date valid or not
# days >= 1 and <=31
# months >= 1 and <=12

def loop():
    loop = input('Type "y" to try again, else press enter to exit\n')
    print()
    if loop == ('y'):
        return main()
    else:
        exit

def correctDay(day):
    if day >=1 and day <=31:
        return True
    else: return False

def correctMonth(month):
    if month >=1 and month <=12:
        return True
    else: return False

def leapYear(year):
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

    if isCentury(year) == True and isDivisible400(year) == True:
        return True
    elif isDivisible4(year) == True:
        return True
    else:
        return False

    

def main():

    day, month, year = input("dd/mm/yyyy: ").split("/")
    day = int(day)
    month = int(month)
    year = int(year)

    if leapYear(year) == True:
        day = day + leapYear(year)
    elif leapYear(year) == False:
        # work in progress. Added functions to see if leap year is true or not. Now to add inn loops to check for months and days in months. feb 28 or 29 etc.
        


    if correctDay(day) == False:
        print("Invalid date.")
    elif correctMonth(month) == False:
        print("Invalid date.")
    else:
        print(f"Valid date of {day:02}/{month:02}/{year:04}.")

    loop()  

if __name__ == '__main__':
    main()