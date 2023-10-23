# lightning-distance.py
#   A program that determines the distance to a lightning strike
#   based on the time elapsed between the flash and the sound of thunder.

#   Info: The speed of sound is approximately 344m/s (1238km/t)

# About program
# Get user input on time elapsed between flash and sound of thunder.
# Calculate distance based on input
# Print out the results to user

def lightning_distance():
    print('A program that determines the distance to a lightning strike ')
    print('based on the time elapsed between flash and sound of thunder.')

    time_elapsed = int(input('How many seconds between flash and sound of thunder? '))

    distance = time_elapsed * 0.344

    print(f'The distance between you and lightning strike is {distance:.1f} kilometer(s).')

lightning_distance()