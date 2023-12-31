# simpleCalculator.py

# display welcome message.
# prompt the user to enter the first number
# prompt the user to enter an operator +,-,*,/
# prompt the user to enter the second number
# perform the calculation based on the operator
# display the result


def perform_addition(n1, n2):
    n3 = n1 + n2
    return n3

def perform_subtraction(n1, n2):
    n3 = n1 - n2
    return n3

def perform_multiplication(n1, n2):
    n3 = n1 * n2
    return n3

def perform_division(n1, n2):
    n3 = n1 / n2
    return n3

def intro():
    print(f"This is a simple calculator that lets you use addition, subtraction, multiplication and division on two numbers.")
    
def main():
    while True:

        try:
            n1 = float(input("Enter first number: "))
            operator = str(input("Enter the operator (+,-,* or /): "))
            n2 = float(input("Enter second number: "))
            
            if operator in ["+", "-", "*", "/"]:
                if operator == "+":
                    result = perform_addition(n1, n2)
                elif operator == "-":
                    result = perform_subtraction(n1, n2)
                elif operator == "*":
                    result = perform_multiplication(n1, n2)
                elif operator == "/":
                    result = perform_division(n1, n2)
                print(f"{n1} {operator} {n2} = {result}\n")
                break
            else:
                print("Invalid operator. Please use +, -, or /.\n")
                
        except ValueError:
            print("Enter a number to use the calculator.\n")
        
        

        restart = input("Press <Enter> to restart, type in \"Q\" or any other letter to quit.\n")
        if restart == "":
            main()
        else:
            quit()

        

if __name__ == "__main__":
    intro()
    main()