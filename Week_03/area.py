"""
Author: Yusuf Hassan
Date: 2025-02-04
Description: This program asks the user for:
    - The measurement unit (inches, feet, centimeters)
    - The length of the rectangle in the units specified by the user.
    - The width of the rectangle in the units specified by the user.
And then calculates the area of the rectangle.
"""

print("Welcome to the Rectangle Area Calculator!")
unit = input("What is your measurement unit (in., ft., cm., etc.)? ")
length = float(input(f'What is the length of the rectangle in {unit}? '))
width = float(input(f'What is the width of the rectangle in {unit}? '))
area = round(length * width, 2)
print('Your rectangle is {:.2f} square {}.'.format(area, unit))
