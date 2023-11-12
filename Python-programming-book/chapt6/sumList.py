# sumList
import math

# A function to summarize the numbers in a list with the sum() function
def sumList(nums):
    Sum = sum(nums)
    return Sum
def main():
    numbers = [4, 9, 16, 25]
    
    print(f"The sum of numbers in the list is: {sumList(numbers)}")
main()