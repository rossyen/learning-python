# exercise14.py
'''
import math

# Loop trough each number in a list and returns the square root of number
def squareEach(nums):
    for i in range(len(nums)):
        nums [i] = math.sqrt(nums[i])

# A function to convert string numbers in a list to integer numbers
def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = float(strList[i])


# A function to summarize the numbers in a list with the sum() function
def sumList(nums):
    Sum = sum(nums)
    return Sum


def main():
    inName = input("Enter name of the file: ")
    data = open(inName, 'r').readline()
    toNumbers(data)
    squareEach(data)
    
    print(f"Sum of square: {sumList(data)}")
          
main()

'''

def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = float(strList[i])

def sumList(nums):
    total = 0
    for n in nums:
        total = total + n
    return total

def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i]**2

def main():
    print("Program to find sum of squares from numbers in a file")
    fname = input("Enter filename: ")
    data = open(fname,'r').readlines()
    toNumbers(data)
    squareEach(data)
    print("Sum of squares:", sumList(data))

main()
