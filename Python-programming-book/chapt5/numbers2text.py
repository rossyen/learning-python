# numbers2text.py
#   A program to convert a sequence of Unicode numbers into
#       a string og text




'''
get the sequence of numbers as a string, inString
split inString into a sequence of smaller strings
message = ''
for each of the smaller strings:
    change the string of digits into the number it represents
    append the Unicode character for that number to message
print message
'''

def main():
    print('This program converts a sequence of Unicode numbers into')
    print('the string of text that it represents. \n')
    
    # get message to encode
    inString = input('Please enter the Unicode-encoded message: ')

    # loop trough each substring and build a Unicode message
    message = ''
    for numStr in inString.split():
        codeNum = int(numStr)               # converts digits to a number
        message = message + chr(codeNum)    # concatenate character to message
        
    print('\nThe decoded message is: ', message)

main()