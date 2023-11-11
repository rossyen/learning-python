# world-count.py
# counts number of lines, words, and characters in a file

def main():
    print("File wordcount")
    print()

    fileName = input("Enter filename: ")
    inFile = open (fileName, 'r')
    characters = inFile.read()
    inFile.close()

    words = characters.split()
    lines = characters.split("\n")

    print("Characters:", len(characters))
    print("Words:", len(words))
    print("Lines:", len(lines))

main()