# Celsius temps to Fahrenheit

def main():
    print('This is a program that converts Celsius to Fahrenheit.')
    celcius = int(input('What is the Celsius temperature? '))
    fahrenheit = 9/5 * celcius + 32
    
    print('The temperature is {} degrees Fahrenheit.'.format(fahrenheit))

main()

input('Press <Enter> key to quit.')