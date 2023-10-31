# dateconvert.py
#   a program that converts dd/mm/yyyy to display "month dd, yyyy"

def main():
    
    dateStr = input('Enter a date (dd/mm/yyyy): ')
    dayStr, monthStr, yearStr = dateStr.split('/')

    months = ["January", "February", "March" , "April " ,
              "May" , "June ", "July", "August ",
              "September", "October" , "November", "December"]
    monthStr = months[int(monthStr)-1]

    print (f'The converted date is: {monthStr} {dayStr}, {yearStr}')

main()
