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



def reverseString(string):
    string = string[::-1]
    string = "".join(string) # string is receives as a list, thats why this is here
    return string

def palindromeTest(one, two):
    return one == two

def stripString(string):
    string = string.lower()
    strippedstring = string.replace(".", "")
    strippedstring = strippedstring.replace(",", "")
    strippedstring = strippedstring.replace(" ", "")
    return strippedstring

def main():
    print("This program lets you see if a word, sentence, number, phrase or a sequence of characters is a palindrome or not.")
    print("Example: The name Otto is spelled Otto backwards.\nThis program excludes spaces, commas, punctuation and uppercase letters.")
    print("So for example if you write: \"ex.t t, ttxe\" it will print out that \"ex.t t, ttxe\" is a Palindrome, since \"exttttxe\" is a Palindrome.\n")
    palindrome = str(input("Input: "))


    
    
    # making letters into a list
    palindromeList = []
    for letter in stripString(palindrome):
        palindromeList.append(letter)
    # if palindrome is even number split in two
    if len(palindromeList) % 2 == 0:
        evenList = len(palindromeList) // 2
        split = reverseString(palindromeList[0:evenList])
        split2 = "".join(palindromeList[evenList:])
        if palindromeTest(split, split2):
            print(f"{palindrome} is a Palindrome")
        else:
            print(f"{palindrome} is NOT a Palindrome")

    # if palindrome is uneven: separate the middle number and split rest in two 
    elif len(palindromeList) % 2 != 0:
        oddList = len(palindromeList) // 2
        split = reverseString(palindromeList[0:oddList])
        split2 = "".join(palindromeList[oddList + 1:])
        if palindromeTest(split, split2):
            print(f"{palindrome} is a Palindrome")
        else:
            print(f"{palindrome} is NOT a Palindrome")

if __name__ == "__main__":
    main()