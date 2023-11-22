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


def main():

    day, month, year = input("dd/mm/yyyy: ").split("/")
    day = int(day)
    month = int(month)
    year = int(year)

    if correctDay(day) == False:
        print("Invalid date.")
    elif correctMonth(month) == False:
        print("Invalid date.")
    else:
        print(f"Valid date of {day:02}/{month:02}/{year:04}.")

    loop()  

if __name__ == '__main__':
    main()