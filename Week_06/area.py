"""
Author: Yusuf Hassan
Date: 2025-02-25
Description: This program calculates the area of a rectangle using functions.
    It validates user input to ensure integer values are entered.
"""

def get_int_input(prompt):
    while True:
        value_str = input(prompt)
        if value_str.isnumeric():
            return int(value_str)
        else:
            print("Invalid input. Please enter a whole number.")

def main():
    print("Welcome to the Rectangle Area Calculator!")
    unit = input("What is your measurement unit (in., ft., cm., etc.)? ")

    length = get_int_input(f"What is the length of the rectangle in {unit}? ")
    width = get_int_input(f"What is the width of the rectangle in {unit}? ")

    area = length * width
    print(f"The area of the rectangle is {area} square {unit}.")

main()