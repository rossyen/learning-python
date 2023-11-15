# Celsius temps to Fahrenheit

def celsiusToFahrenheit(celsius):
    fahrenheit = 9.0/5.0 * celsius + 32
    return fahrenheit


def main():
    
    celsius = int(input('What is the Celsius temperature? '))
    fahrenheit = celsiusToFahrenheit(celsius)
    print(f'The temperature is {fahrenheit:.2f} degrees Fahrenheit.')   
    
    # Print warming for extreme temps
    if fahrenheit > 90:
        print("It's really hot out there. Be careful!")
    if fahrenheit < 30:
        print("Brrrrr. Be sure to dress warmly")

    '''
    Commented out temperature list.

    temp_list = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print('Lists temperature from celsius to fahrenheit in a list from 0 to 100 in intervals of 10: ')
    for x in temp_list:
        print(x,end='   ')
        for i in range(1):
            print(9.0/5.0 * int(x) + 32)
'''

if __name__ == '__main__':
    main()



