# quizScore.py
# A program that gives out a score based on user input

# receive input on quiz score as an int

# use decision structure do decide which score to give based on input

# print result to user


def loop():
    loop = input('Type "y" to try again, else press enter to exit\n')
    print()
    if loop == ('y'):
        return main()
    else:
        exit

def grades(score):
    
    if score == 5:
        return "A"
    elif score == 4:
        return "B"
    elif score == 3:
        return "C"
    elif score == 2:
        return "D"
    elif score <= 1:
        return "F"
    else:
        print("Enter a number between 0 and 5 do get a grade.")
        return "invalid"
    

def main():
    
    try:
        score = int(input("What score did you get? "))
        print(f"The score on your quiz is {grades(score)}.")
    except ValueError:
        print("Please enter a valid integer.") 

    loop()  

if __name__ == '__main__':
    main()