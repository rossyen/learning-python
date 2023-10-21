# This is a program that converts temperatures from Fahrenheit to Celsius

# This program will loop trough either a list of 10 temperatures
# or give the user an option to choose to convert temperature

# def a function
def main():

# Get user input if they want to convert temperature or see standard conversion
    print('To convert temperatures from fahrenheit to celsius type "y" ')
    print('If you want to see some random temperature conversions type "n" ')

# Receive input and store in variable    
    user_input = str(input('Else press "enter" to exit program: '))

# if answer is qual to y convert fahrenheit to celsius
    if (user_input == 'y'):
        fahrenheit = int(input('Type in fahrenheit to convert to celsius: '))
        celsius = (fahrenheit-32)/1.8 
        print(f'{fahrenheit} degrees fahrenheit equals {celsius:.2f} degrees celsius ')

# if answer is equal to n show list that converts for user 
    elif (user_input == 'n'):
        temp_list = [-10, 0, 10, 20, 30, 40, 50, 60, 70]
        for x in temp_list:
            print(x,end='   ')
            for i in range(1):
                print((int((x)-32)/1.8))
        return
# else return to menu    
    else:
        return

main()