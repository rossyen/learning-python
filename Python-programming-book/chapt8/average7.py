# average7.py

def main():
    fileName = input("What file are the numbers in=?" )
    inFile = open(fileName, 'r')
    total = 0.0
    count = 0
    line = inFile.readline()
    while line != "":
        # update total and count for value in line
        for xStr in line.split(","):
            total = total + float(xStr)
            count = count + 1
        line = inFile.readline()
    print("\nThe average of the numbers is", total / count)

main()

