# strnumToInt.py
# A test program to converting a string list of numbers into numbers

# A function to convert string numbers in a list to integer numbers
def toNumbers(strList):
    for i in range(len(strList)):
        strList [i] = int(strList[i])
    return strList

def main():
    strList = ["1", "2", "3"]

    print(toNumbers(strList))

main()