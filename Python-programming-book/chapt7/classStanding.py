# classStanding.py

# A program to calculate class standing from the number of credits earned

# receive input on credits earned

# check to see if credits match any of these statements
# less then 7 = Freshman
# 7-15 = Sophomore
# 16-25 = Junior
# >= 26 = Senior

# enter output to user

# homemade loop to check for errors and quickly test the code with different input.
def loop():
    loop = input('Type "y" to try again, else press enter to exit\n')
    print()
    if loop == ('y'):
        return main()
    else:
        exit

def classStanding(credits):
    
    if credits < 7:
        return "Freshman"
    elif credits >= 7 and credits <= 15:
        return "Sophomore"
    elif credits >= 16 and credits <= 25:
        return "Junior"
    elif credits >= 26:
        return "Senior"
    else:
        print("Enter your credits earned to view class.")
    

def main():
    
    try:
        credits = int(input("What credits do you have? "))
        classClassifier = classStanding(credits)          
        print(f"This makes you a {classClassifier}.")
    except ValueError:
        print("Please enter a valid integer to determine your student classification.") 

    loop()  

if __name__ == '__main__':
    main()

