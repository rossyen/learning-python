# commonElementsFinder.py

# a program that takes two list as input and outputs a new list containing
# the common elements between the two input lists.

def common_elements_finder(l1, l2):
    newList = [x for x in l1 if x == x in l2]
    return newList

def main():

    list1 = input("Enter numbers to add into list(Split numbers by space \" \": ").split(" ")
    list2 = input("Enter numbers to add into list(Split numbers by space \" \": ").split(" ")
    print(f"Common elements in the two lists are:\n{common_elements_finder(list1, list2)}")

if __name__ == "__main__":
    main()