# average2.py

def main():
    total = 0.0
    count = 0
    moreData = "yes"
    while moreData[0] == "y":
        x = float(input("Enter a number >> "))
        total = total + x
        count = count + 1
        moreData = input("Do you have more numbers (yes or no)? ")
    print("\nThe average of the numbers is", total/count)

main()