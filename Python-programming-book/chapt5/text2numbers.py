'''
get the message to encode

for each character in the message:
    print the letter number of the character

message = input('Please enter the message to encode: ')

for ch in message:


'''

# text2numbers.py
#   A program that converts a textual message into a sequence of
#       numbers, utilizing the underlying Unicode encoding.

def main():
    print('This program converts a textual message into a sequence')
    print('of numbers representing the Unicode encoding of the message. \n')

    # Get message to encode
    message = input('Please enter the message to encode: ')

    print('\nHere are the Unicode codes:')

    # Loop trough the message and print out the Unicode values
    for ch in message:
        print(ord(ch), end=' ')
    
    print() # blank line before prompt

main()
