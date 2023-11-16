# speedTicketCalculator.py
# A program to print if speed is legal, or the amount of the fine

# Ticket fine policy in Podunksville is 50$
# plus 5$ for each mph over limit
# plus 200$ for and speed over 90mph

# receive input on speed and speed limit

# output either speed is legal or print amount of fine, if illegal speed




# homemade loop to check for errors and quickly test the code with different input.
def loop():
    loop = input('Type "y" to try again, else press enter to exit\n')
    print()
    if loop == ('y'):
        return main()
    else:
        exit

def speedTicket(speed, speedLimit):
    ticket = 50
    loopRange = speed - speedLimit
    for i in range(loopRange):
        ticket = ticket + 1
    if speed >90:
        ticket = ticket + 200
        return ticket
    else:
        return ticket
        
    
def main():
    
    try:
        speedLimit = int(input("Enter the speed limit: "))
        speed = int(input("Enter your speed: "))
        maxSpeed = 80
        if speedLimit > maxSpeed:
            print("The max speed limit is 80 mph. Try again.")
        elif speed <= maxSpeed:
            print("Your speed is within the speed limit.")
        else:
            print(f"Your speed is above the speed limit and your fine is: {speedTicket(speed, speedLimit)}$")

    except ValueError:
        print("Enter a valid integer as speed limit and speed. ") 

    loop()  

if __name__ == '__main__':
    main()

