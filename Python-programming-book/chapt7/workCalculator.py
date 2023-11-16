# workCalculator.py
# A calculator to determine payment after a weeks worth (37,5 hours)
# If working more then 37,5 hours the pay increase by 50%


# receive input on hours worked

# receive input on hourly rate
    
# create a function for calculating hourly wages
# use if statement calculating to calculate both normal hours
# and overtime ours

# print output to user
def payment(hours, rate):
    if hours <= 37.5:
        pay = hours * rate
        return pay
    else:
        pay = hours * rate
        extraPay = (hours - 37.5) * rate * 1.5
        overTime = pay + extraPay
        return overTime
    
def main():

    hours = input("How many hours have you worked this week? ")
    hourlyRate = input("What is your hourly rate? ")
    hours = float(hours)
    hourlyRate = float(hourlyRate)

    expectedPay = payment(hours, hourlyRate)
    print(f"For {hours} work this week you will receive {expectedPay} (before taxes).")

if __name__ == '__main__':
    main()