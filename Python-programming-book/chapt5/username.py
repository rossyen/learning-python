# username.py
#   Simple string processing program to generate usernames.

def main():
    print('This program generates computer usernames.\n')

    # Get users' first and last name
    first = input('Please enter you first name: ').lower()
    second = input('Please enter you last name: ').lower()

    # concatenate first and initial with 7 chars of the last name.
    uname = first [0] + second [:7]

    #output username
    print(f'Your username is {uname}')

main()