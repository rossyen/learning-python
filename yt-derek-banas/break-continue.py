# continue is going to stop executing the code that remains in the loop
# and start at the top of the loop

# break is going to exit the loop

i = 1

while i <= 20:
    if (i % 2) == 0:
        i += 1
        continue

    if i == 15:
        break

    print('odd : ', i)

    i += 1