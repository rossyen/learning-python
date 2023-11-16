# examScore.py
# A program that gives out a score based on user input

# receive input on quiz score as an int

# use decision structure do decide which score to give based on input
# if 90-100:A
# elif 80-89:B
# elif 70-79:C
# elif 60-69:D
# else <60:F

# print result to user


def loop():
    loop = input('Type "y" to try again, else press enter to exit\n')
    print()
    if loop == ('y'):
        return main()
    else:
        exit

def grades(score):
    
    if score >= 90 and score <= 100:
        return "A"
    elif score >= 80 and score <= 89:
        return "B"
    elif score >= 70 and score <= 79:
        return "C"
    elif score >= 60 and score <= 69:
        return "D"
    elif score < 60:
        return "F"
    else:
        print("Enter a number between 0 and 100 to get a grade.")
        return "invalid with given number."
    

def main():
    
    try:
        score = int(input("What score did you get on your exam? "))
        print(f"The grade on your exam is {grades(score)}.")
    except ValueError:
        print("Please enter a valid integer to determine your grade.") 

    loop()  

if __name__ == '__main__':
    main()