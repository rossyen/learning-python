# This is a program that converts megabytes to gigabytes
def bytes_converter():
# Print presentation of program to user
    print('This is a small program to let you convert megabytes to gigabytes.')

# Ask user to convert megabytes to gigabytes and store in a variable

    for i in range(1):
        megabytes = int(input('Enter megabytes to see how many gigabytes it is: '))
        
# Convert megabytes to gigabytes

        gigabytes = megabytes / 1024

# print result to user

        print(f'{megabytes} megabytes equals {gigabytes:.2f} gigabytes.')

bytes_converter()

print('Press "Enter" to quit program.')