# This program converts miles to kilometer
# One kilometer is approximately 0.62 miles

def miles_km_converter ():
# Present program to user
    print('This is a program to convert miles to kilometer.')

# Ask user for input on conversion
    for i in range (1):
        miles = int(input('Input miles to get kilometer: '))
        
        
    # Convert miles to km
        kilometers = miles * 0.62

# Print result to user
        print(f'{miles} miles equals  {kilometers} kilometers ')

miles_km_converter()

input('Press "Enter" key to quit.')