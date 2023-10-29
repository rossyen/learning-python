# numbers2text2.py
#   A program to convert a sequence of Unicode numbers into
#       a string of text. Efficient version using a list accumulator.

def main():
    print('This program converts a sequence of Unicode numbers into')
    print('the string of text that it represents.\n')

    # Get the message to encode
    inString = input('Please enter the Unicode-encoded message: ')

    # loop trough each substring and build Unicode message
    chars = []
    for numStr in inString.split():
        codeNum = int(numStr)