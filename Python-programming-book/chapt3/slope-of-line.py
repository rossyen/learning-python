# slope-of-line.py
#   A program that calculates the slop of a line trough two
#   non-vertical points entered by the user.

# Get user coordinates
# Calculate slope of a line
# Print output to user

def slope_line():
    print('To see the slope of a line. Enter numbers so we can calculate it for you.')
    x1, y1 = (input('Enter starting coordinates: ').split())
    x2, y2 = (input('Enter stop coordinates: ').split())
    x1 = int(x1)
    x2 = int(x2)
    y2 = int(y2)
    y1 = int(y1)

    slope = (y2 - y1)/(x2 - x1)
    print(f'The slope is {slope:.2} steep.')

slope_line()