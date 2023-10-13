# Case nr 2:
# If age is 5 Go to Kindergarten
# Ages 6 trough 17 goes to grades 1 trough 12
# If age is greater then 17 say go to college
# Try to complete with 10 or less lines


# Receive age and store in age
age1 = eval(input('Enter age to see what you should do: '))

# Define variable grades 1-12

grade1 = int(age1 - 5)

# if age is equal to 5 say Go to Kindergarten
if (age1 == 5):
    print('Go to Kindergarten')
# if age >= 6 and not <18 say go to grade 1 trough 12
elif (age1 >= 6 ) and (age1 <18):
    print(f'Go to grade {grade1}')
# if age is greater then 17 say go to collage
elif (age1 > 17):
    print('Go to college')
# else you are too young
else:
    print('You are too young')

