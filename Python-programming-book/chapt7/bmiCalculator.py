# bmiCalculator.py

# A calculator to determine if you are above, within, or below healthy BMI range


# homemade loop to check for errors and quickly test the code with different input.
def loop():
    loop = input('Type "y" to try again, else press enter to exit\n')
    print()
    if loop == ('y'):
        return main()
    else:
        exit

def BMIcalculator(weight, height):
    BMI = weight/((height/100)**2)
    return BMI
    
def main():
    
    try:
        weight = float(input("Please enter your weight in kg: "))
        height = float(input("Please enter your height in cm: "))
        BMI = BMIcalculator(weight, height)
        if height < 3:
            print("Enter your height in cm, not meters.")
        else:
            if BMI <19:
                print(f"Your BMI of {BMI:.2f} is below the healthy range.")
            elif BMI >25:
                print(f"Your BMI of {BMI:.2f} is above the healthy range.")
            else:
                print(f"You have a healthy BMI of {BMI:.2f}")
    except ValueError:
        print("Please enter a valid integer to determine your BMI.") 

    loop()  

if __name__ == '__main__':
    main()

