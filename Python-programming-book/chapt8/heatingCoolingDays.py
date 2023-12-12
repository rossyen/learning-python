# heatingCoolingDays.py

# Get input on average daily temperature
# loop input to receive input until user uses the stop function
# if average temperature is < 60 add to total of heating days
# if average temp > 80 add to total of cooling days
# if temp >=60 and <=80 continue loop and ask for more temp days
# print two totals after all data has been processed


def main():
    fileName = input('What file are the numbers in? ')
    inFile = open(fileName, 'r')

    heatingDays = 0
    coolingDays = 0

    for line in inFile:
        print(f'Current line: {line}')
        temp = line.strip()
        if temp == "":
            continue

        tempInt = int(temp)
        if tempInt < 60:
            heatingDays = heatingDays + 1 
        elif tempInt > 80:
            coolingDays = coolingDays + 1

    print(f"Number of cooling days: {coolingDays}\n Number of heating days: {heatingDays}")
    inFile.close()
main()