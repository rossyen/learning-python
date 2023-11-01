# test-loop.py
# A program that lets me run and troubleshot other programs
# instead of writing a loop for testing

def loop():
    loop = input('Type "y" to try again, else press enter to exit\n')
    print()
    if loop == ('y'):
        return main()
    else:
        exit

loop()