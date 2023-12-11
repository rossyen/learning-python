# heatingCoolingDays.py

# Get input on average daily temperature
# loop input to receive input until user uses the stop function
# if average temperature is < 60 add to total of heating days
# if average temp > 80 add to total of cooling days
# if temp >=60 and <=80 continue loop and ask for more temp days
# print two totals after all data has been processed


def main():

    heatingDays = 0
    coolingDays = 0
    while True:
        temp = input("Enter temperature: (<Enter> to quit) >> ")
        if temp == "":
            break

        tempInt = int(temp)
        if tempInt < 60:
            heatingDays = heatingDays + 1
        elif tempInt > 80:
            coolingDays = coolingDays + 1

    print(f"Number of cooling days: {coolingDays}\n Number of heating days: {heatingDays}")

main()