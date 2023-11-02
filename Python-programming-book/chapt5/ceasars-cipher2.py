# ceasars-cipther2.py
#   A program to encode and decode a phrase with a given key

'''
Algorithm:

Receive phrase to encode or decode from user and store in phrase
Receive key from user and store in key
Make a string containing all characters of alphabet
Determine value of each chr in string phrase and make each
chr a = 0, b = 1 etc
Loop the phrase numbers with the alphabet string to get encoded/decoded message
with key added or subtracted  

print out the encoded or decoded message to user

'''

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

    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz'
    # get phrase to encrypt
    phrase = input('Please enter message to encode: ').lower()
    
    # get key for encrypting 
    key = input('Please enter the key for encryption: ')
    key = int(key)

    cipher = ''
    for letter in phrase:
        pos = alphabet.find(letter)
        newpos = (pos + key) % len(alphabet)
        cipher = cipher + alphabet[newpos]


    print('Encoded message follows:')
    print(cipher)
    
    loop()

main()