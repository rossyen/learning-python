# wordFrequencyCounter.py

# A program that takes a sentence or paragraph as input from the user
# and counts the frequency of each word. 
# The program should output a list of unique words along with their
# respective frequencies.



# accept a sentence or paragraph as input from the user
# Tokenize the input into words (ignoring punctuation and considering case-insensitivity)
# Count the frequency of each unique word
# output a list of unique words and their frequencies

def clean_string(string):
    originalString = string
    specialCharacters = ".,"
    cleanedString = originalString
    for char in specialCharacters:
        cleanedString = cleanedString.replace(char, "")
    
    return cleanedString.lower()



def main():
    phrase = str(input("Enter sentence or paragraph: \n>>> "))
    phrase = clean_string(phrase)
    phrase = phrase.split(" ")
    lst = {}
    for word in phrase:
        lst[word] = lst.get(word, 0) + 1

    print("Word Frequency:")
    for word, count in lst.items():
        print(f" {word}: {count}")

        
if __name__ == "__main__":
    main()