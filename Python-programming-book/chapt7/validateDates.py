# validateDates.py

def loop():
    loop = input('Type "y" to try again, else press enter to exit\n')
    print()
    if loop == ('y'):
        return main()
    else:
        exit

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

def validateDate(day, month, year):
        day = int(day)
        month = int(month)
        year = int(year)

        if leapYear(year) == False:
            if day >= 1 and day <= 31 and month in [1, 3, 5, 7, 8, 10, 12]:
                return(f"Valid date of {day:02}/{month:02}/{year:04}.")
            elif day >= 1 and day <= 28 and month == 2:
                return(f"Valid date of {day:02}/{month:02}/{year:04}.")
            elif day >= 1 and day <= 30 and month in [4, 6, 9, 11]:
                return(f"Valid date of {day:02}/{month:02}/{year:04}.")
            else:
                return("Invalid date.")
        elif leapYear(year) == True:
            if day >= 1 and day <= 31 and month in [1, 3, 5, 7, 8, 10, 12]:
                return(f"Valid date of {day:02}/{month:02}/{year:04}.")
            elif day >= 1 and day <= 29 and month == 2:
                return(f"Valid date of {day:02}/{month:02}/{year:04}.")
            elif day >= 1 and day <= 28 and month in [4, 6, 9, 11]:
                return(f"Valid date of {day:02}/{month:02}/{year:04}.")
            else:
                return("Invalid date.")

def main():
    
    try:
        day, month, year = input("dd/mm/yyyy: ").split("/")
        day = int(day)
        month = int(month)
        year = int(year)
        print(validateDate(day, month, year))


        # Prints corresponding day number in the year. 
        dayNum = 31*(month - 1) + day
        
        if month > 3 and month <= 12:
            dayNum = dayNum - (4*(month)+23)//10
            if leapYear(year) == True and month > 2 and month <=12:
                dayNum = dayNum + 1
                print(f"Corresponding day number is {dayNum}.")
            else:
                print(f"Corresponding day number is {dayNum}.")
        else:
            print(f"Corresponding day number is {dayNum}.")
            
        
        # Calculate the corresponding day number after validating the date
        # three steps using int arithmetic: 
        # dayNum = 31(month - 1) + day
        # if month is after feb subtract (4(month)+23)//10
        # if it's a leap year and after feb 29, add 1
        
    except ValueError:
        print("Error!\nPlease enter a date in dd/mm/yyyy format.")
    

    loop()  

if __name__ == '__main__':
    main()