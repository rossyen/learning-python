# acronym.py
# This program creates acronyms from user input
# and prints a all uppercase acronym as output

'''
get input, store in list as str and split input with (' ')

print list with .first and .upper so that output only prints first letter of words in uppercase

'''
def loop():
    loop = input('Type "y" to try again, else press enter to exit\n')
    print()
    if loop == ('y'):
        return main()
    else:
        exit

def main():

    # get input from user

    phrase = str(input('Enter a phrase to make it an acronym: \n'))
    
    acronym = phrase.split()
    first_letters = [word[0] for word in acronym]
    first_letters_str = ''.join(first_letters)

    print(first_letters_str.upper())
    loop()     
main()