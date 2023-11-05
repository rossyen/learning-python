# word-length.py
# A program that calculates the average word length in a sentence entered by the user


# Intro to program
import statistics

def main():
    print('Word average length counter')
    print()


    # Receive phrase from user
    phrase = input('Enter a phrase: ')
    
    # using accumulator loop
    count = 0
    total = 0
    for word in phrase.split():
        total = total + len(word)
        count = count + 1

    print(f'Average word length in sentence: {total/count:.3}')

main()