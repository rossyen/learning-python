# Celsius temps to Fahrenheit

def main():
    print('This is a program that converts Celsius to Fahrenheit')
    print('and shows a list from 0 to 100 Celsius converted in intervals of 10: ')

    for i in range (5):
        celsius = int(input('What is the Celsius temperature? '))
        fahrenheit = 9/5 * celsius + 32
        print('The temperature is {} degrees Fahrenheit.'.format(fahrenheit))   
    
    temp_list = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print('Lists temperature from celsius to fahrenheit in a list from 0 to 100 in intervals of 10: ')
    for x in temp_list:
        print(x,end='   ')
        for i in range(1):
            print(9/5 * int(x) + 32)

main()

input('Press <Enter> key to quit.')

