# word-counter.py
# A program that counts words in sentence

def main():
    print('Word counter')
    print()

    phrase = input('Enter a phrase: ')

    # using a accumulator loop
    count = 0
    for i in phrase.split():
        count = count + 1
    print(f'Number of words: {count}')

main()