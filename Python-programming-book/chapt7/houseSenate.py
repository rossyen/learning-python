# houseSenate.py
# A program to determine if a person is eligible for Senate and House
# For US senator 30 years old and 9 years US citizen
# For US representative 25 years old and 7 years US citizen

# receive input on both age and number of years US citizen

# test to see if age >= 25
# test to see if age >= 30
# test if US citizen >= 7
# test if US citizen >= 9

def loop():
    loop = input('Type "y" to try again, else press enter to exit\n')
    print()
    if loop == ('y'):
        return main()
    else:
        exit

def main():
    print("This is a program to let you know if you are eligible to be a Senator or US representative\n")
    age = int(input("Please enter your age: "))
    citizen = int(input("Please enter how many years you've been a US citizen: "))
    
    if age < 25 and citizen <7:
        print("You are not eligible for the Senate or House")
    elif age >= 25 and citizen >= 7:
        print("You are eligible to become a US representative")
    elif age >= 30 and citizen >= 9:
        print("You are eligible to become a US senator")
    else:
        print("You are not eligible for the Senate or House")
        print("Age limit is 25 for US representative, and 30 for Senator")
        print("You must have been a US citizen for 7 years to represent the House and 9 to represent the Senate")


    loop()  

if __name__ == '__main__':
    main()