import pyinputplus as pyip

# 1. Write a program that asks the user to enter a number and then prints the number multiplied by 2.
def multiply_by_two():
    myString = pyip.inputTime("Enter Time: ", format='%H:%M:%S')
    print('My date:', myString)

if __name__ == "__main__":
    multiply_by_two()