# month2.py
#   A program to print the month abbreviation, given its number.

def main():

    # months is a list used as a lookup table
    months = ["January", "February", "March" , "April " ,
              "May" , "June ", "July", "August ",
              "September", "October" , "November", "December"]
    
    n =int(input('Enter a month number (1-12): '))
    print()

    print('The month abbreviation is', months[n-1] + '. \n')

main()    

input('Press enter to exit.')