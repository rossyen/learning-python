# month.py
#   A program to print the abbreviation of a month, given its number

def main():
    months = 'JanFebMarAprMayJunJulAugSepOctNovDec'
    print('This is a program that lets you see what month you are in by typing its number.\n')

    n = int(input('Enter a month number (1-12:) '))

    # compute starting position of a month in n months
    pos = (n-1) * 3
    
    # Grab the appropriate slice from months 
    monthAbbrev = months[pos:pos+3]

    # print the result
    print(f'The month abbreviation is {monthAbbrev}.\n')

main()

input('Press enter to exit.')