# word-counter.py
#   A program that counts words entered by user


def main():
# Intro to program
    print('This program lets you see how many words you have type in')
    print()

# Ask user for input on words to count and store in a variable
    sentence = input('Please type your sentence: \n')

# make variable a list
    slenght = sentence.split()
    slist = [word[0] for word in slenght]
    slistcount = ''.join(slist)
   
# # count words in list and print number of words in list
    print(f'Your sentence has {len(slistcount)} words in it')

main()
