# grade2.py
#   A program to grade 100-point exams on a the scale
#   90-100:A, 80-89:B, 70-79:C, 60-69:D, <60:F.


def loop():
    loop = input('Type "y" to try again, else press enter to exit\n')
    print()
    if loop == ('y'):
        return main()
    else:
        exit

def main():
    
    # receive input from user on how many points on exam
    score = int(input('What score did you get on exam?\n'))
    
    # make a variable of grades and multiply each string so it fits the score with number
    # of letter in each score. 

    grades = 60*'F'+10*'D'+10*'C'+10*'B'+11*'A'

    # print out the grade with a list manipulation
    # the manipulation makes the score variable select the number
    # the characters have in the grade string.
    print (f'The grade on your exam is {grades[score]}')
    
    loop()

main()
