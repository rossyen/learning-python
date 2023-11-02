# ceasars-cipher.py
# A program to encode a phrase with a given key
# and print out the encoding


def loop():
    loop = input('Type "y" to try again, else press enter to exit\n')
    print()
    if loop == ('y'):
        return main()
    else:
        exit

def main():
    print('This program lets you encode a phrase with a key')
    print('To see the encrypted message: use the negative key')

    # get phrase to encrypt
    word = input('Please enter message to encode: ')

    # get key for encrypting 
    key = input('Please enter the key for encryption: ')
    key = int(key)

    # loop trough message and print out the unicode values + key
    for ch in word:
        print(chr(ord(ch) + key), end='')
    print()
    
    loop()

main()