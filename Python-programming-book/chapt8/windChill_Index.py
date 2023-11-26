# windChill_Index.py

# prints a table of windchill values
# Formula only works if wind speed is in excess of 3 mph

# Formula:
# 35.74 + 0.6215*T - 35.75(V**0.16) + 0.4275(V**0.16)
# T = temperature in Fahrenheit, and V is the wind speed in miles per hour

# We want to print out a nicely formatted table of windchill values.
# Rows should represent:
# Side colum: wind speed from 0 to 50 in 5-mph increments

windSpeed = 0
temperature = 70

# Top colum: temperature from -20 to +60 in 10-degree increments 
for i in range (9):
    temperature = temperature - 10
    print(f'{temperature}', end="\t")