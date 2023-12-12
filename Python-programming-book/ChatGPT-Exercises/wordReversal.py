# wordReversal.py

# take sentence as input from user
# output the same sentence with the words reversed
# example: input "Hello World", output "World Hello"

def wordReversal(sentence):
    sentence = sentence
    reversedSentence = sentence.split()
    reversedSentence = reversedSentence[::-1]
    reversedSentence = " ".join(reversedSentence)
    return reversedSentence
    

def main():
    sentence = str(input("Enter a sentence to see words reversed:+\n"))
    sentence = wordReversal(sentence)
    print(sentence)

if __name__ == "__main__":
    main()