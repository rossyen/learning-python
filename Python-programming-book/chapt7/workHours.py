# workHours.py

# A program that calculates the total bill of hours in work
# Starting and ending times are in single 24-hours period
# Partial hours should be appropriately prorated

# Charge 2.50$ until 09:00 PM
# after 09:00 PM rate drops to 1.75$ an hour

# Receive input on starting time 12:00 format
# Receive input on end time 12:00 format

# If ending time har larger number of minutes:
# subtract the starting time from the ending time

# if starting time har larger number of minutes:
# add 60 minutes to the ending hour and subtract 1 hour from ending time.
# subtract the new ending time number with starting time to see result

# homemade loop to check for errors and quickly test the code with different input.


def loop():
    loop = input('Type "y" to try again, else press enter to exit\n')
    print()
    if loop == ('y'):
        return main()
    else:
        exit
    
def main():
    print("Babysitting Calculator\n")
    print("Enter times using 24 hour format (e.g. 8pm is 20:00)")
    startingHours, startingMinutes = input("Starting time (hh:mm): ").split(":")
    endingHours, endingMinutes = input("Ending time (hh:mm): ").split(":")
    
    start = int(startingHours) + float(startingMinutes)/60.0
    end = int(endingHours) + float(endingMinutes)/60.0

    if end < start:
        end = end + 24

    bedtime = 21.0
    if start < bedtime:
        if end < bedtime:
            primeHours = end - start
            extraHours = 0.0
        else:
            primeHours = bedtime - start
            extraHours = end - bedtime
    else:
        primeHours = 0.0
        extraHours = end - start

    pay = 2.50 * primeHours + 1.75 * extraHours
    primeHours(f"Total payment due: ${pay:.2f}")
    loop()  

if __name__ == '__main__':
    main()

