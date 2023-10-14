# Did not manage case on my own.
'''
How tall is the tree: 5

    #
   ###
  #####
 #######
#########
    #
'''
# Use 1 while loop and 3 for loops
# 4 spaces : 1 hash
# 3 spaces : 3 hashes
# 2 spaces : 5 hashes
# 1 space : 7 hashes
# 0 spaces: 9 hashes

# first and last 

# Need to do:
# 1. Decrement/reduce spaces by 1 each time trough loop
# 2. Increment the hashes by 2 each time trough the loop
# 3. Save the spaces to the stump by calculating tree height -1
# 4. Decrement/reduce from the height until it equals 0
# 5. Print spaces and then hashes for each row
# 6. Print stump spaces and then 1 hash

# Get the number of rows for the tree:

tree_hight = input('How tall do you want the tree to be: ')

# Convert into and integer

tree_hight =int(tree_hight)

# Get the starting spaces for the top of the tree
spaces = tree_hight - 1

# There is on hash to start that will be incremented
hashes = 1

# Save stump spaces for later
stump_spaces = tree_hight - 1

# Make sure the right number of rows are printed
while tree_hight != 0:

# Print the spaces
# print('',end="") breaks and starts a new line
    for i in range(spaces):
        print(' ', end='')

# Print the hashes
    for i in range(hashes):
        print('#', end='')

# Newline after each row is printed
    print()

# The spaces is decremented by 1 each time
    spaces -= 1

# That hashes is incremented by 2 each time
    hashes += 2

# Decrement tree height each time to jump out of the loop
    tree_hight -= 1

# Print the spaces before the stump and the hash
for i in range(stump_spaces):
    print(' ', end='')

print('#')