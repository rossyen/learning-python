# palindromeChecker.py

# Checks if a given string is a palindrome.
# A palindrome is a word, phrase, number, or other sequence of characters
# that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

# receive input to check if palindrome
# clean string for "," spaces, "." etc.
# read len(sentence) on sentence to determine length
# split str in two on half length determined by len()
# reverse one of new strings
# check with bool if both strings are equal
# print output if equal or not

def wordReversal(sentence):
    sentence = sentence
    reversedSentence = sentence.split()
    reversedSentence = reversedSentence[::-1]
    reversedSentence = " ".join(reversedSentence)
    return reversedSentence


def main():
    palindrome = str(input("Enter a word, phrase, number, or other sequence of characters\n to see if its a palindrome or not.\n:"))
    palindrome = palindrome.lower()
    strippedPalindrome = palindrome.replace(".", "")
    strippedPalindrome = strippedPalindrome.replace(",", "")
    strippedPalindrome = strippedPalindrome.replace(" ", "")

    print(strippedPalindrome, len(strippedPalindrome))

main()
