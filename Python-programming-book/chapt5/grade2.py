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

def grade(score):
    grades = 60*'F'+10*'D'+10*'C'+10*'B'+11*'A'
    grades = grades[score]
    return grades

def main():
    
    score = int(input('What score did you get on exam?\n'))
    
    print (f'The grade on your exam is {grade(score)}')
    
    loop()

main()
