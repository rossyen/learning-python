# grade.py
#   A program that grades quizzes on a scale of
#   5-A, 4-B, 3-C, 2-D, 1-F, 0-F

def main():
    # get score number from user
    score = input('What score did you receive on your quiz? ')
    
    # list of grades
    grades = ['F', 'F', 'D', 'C', 'B', 'A']

    # convert score variable to a grade
    score = grades[int(score)]

    # print grade

    print(f'The grade on your quiz is: {score}')
    print()

main()

def loop():
    loop = input('Type "y" to try again, else press enter to exit\n')
    print()
    if loop == ('y'):
        return main()
    else:
        exit

loop()