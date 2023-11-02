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
    
    name = input('Enter a name: ')
    
    ''' namesplit = name.split(' ')
    fullnamelist = [word[:] for word in namesplit]
    fullname = ''.join(fullnamelist)
    print(fullname) '''
    # shorter code than the one commented out 
    fullname = ''.join(name.split())

    total = 0
    for letter in fullname:
        total = total + ord(letter.lower()) - ord('a') + 1
    print(f'The value is: {total}')
    loop()    
main()

    