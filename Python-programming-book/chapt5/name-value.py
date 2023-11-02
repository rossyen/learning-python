# name-value.py
#   A program to determinate a person's character traits based on the
#   numeric value of a name

def loop():
    loop = input('Type "y" to try again, else press enter to exit\n')
    print()
    if loop == ('y'):
        return main()
    else:
        exit


def main():
    
    name = input('Enter a single name: ')
    total = 0
    for letter in name:
        total = total + ord(letter.lower()) - ord('a') + 1
    print(f'The value is: {total}')
    loop()    
main()

    