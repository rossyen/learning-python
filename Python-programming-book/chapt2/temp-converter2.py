# This is a program that converts temperatures from Fahrenheit to Celsius

# This program will loop trough either a list of 10 temperatures
# or give the user an option to choose to convert temperature

# def a function
def main():

# Get user input if they want to convert temperature or see standard conversion
    print('To convert temperatures from fahrenheit to celsius type "y" ')
    print('If you want to see some random temperature conversions type "n" ')

# Receive input and store in variable    
    y, n = (input('Else press "enter" to exit program: ')).split()

# if answer is qual to y convert fahrenheit to celsius
    if (y == str(y)):
        fahrenheit = int(input('Type in fahrenheit to convert to celsius: '))
        celsius = (fahrenheit-32)/1.8 
        print(f'{fahrenheit} degrees fahrenheit equals {celsius:.2f} degrees celsius ')
        return
# if answer is equal to n show list that converts for user 
    elif (n == str(n)):
        temp_list = [-10, -5, 0, 5, 10, 15, 20, 25, 30]
        for x in temp_list:
            print(x,end='   ')
            for i in range(1):
                print((float((fahrenheit)-32)/1.8))
        return
# else return to menu    
    else:
        return

main()