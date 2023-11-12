# squareList.py
# A script to square each number in a list

import math

# Loop trough each number in a list and returns the square root of number
def squareEach(nums):
    for i in range(len(nums)):
        nums [i] = math.sqrt(nums[i])
    return nums


def main():
    numbers = [4, 9, 16, 25]

    print(f"Square root of numbers: {squareEach(numbers)}")

main()