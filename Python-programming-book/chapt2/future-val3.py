# Make a program that shows a fixed invested amount
# every year over 'x' times year

# Print welcome message
def main():
    print('This is a program')
# Get input on fixed investment amount
    f_inv = int(input('How much do you want to save annually: '))

# Get interest rate
    i_rate = float(input('What interest rate do you expect: '))

# Get input on how many years to save
    n = int(input('How many years are you planning to save: '))

    final_sum = f_inv*(1 + i_rate/1)**1

# print amount saved on fixed investment over 'x' times years
    for i in range(n):
        final_sum = (final_sum*(1 + i_rate/1)**1)+f_inv

    print(f'Earning you {final_sum:.2f} over {n} years')

main()