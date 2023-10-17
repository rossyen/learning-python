# Celsius temps to Fahrenheit

def main():
    print('This is a program that converts Celsius to Fahrenheit.')
        
    for i in range (5):
        celsius = int(input('What is the Celsius temperature? '))
        fahrenheit = 9/5 * celsius + 32
        print('The temperature is {} degrees Fahrenheit.'.format(fahrenheit))   
    

main()

input('Press <Enter> key to quit.')

