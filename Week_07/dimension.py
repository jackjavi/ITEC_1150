"""
Author: Yusuf Hassan
Date: 2025-03-04
Description: This program calculates the width of a rectangle given its area and length.
  It uses functions and exception handling for input validation and calculations.
"""

def get_numeric_input(prompt):
    """
    Gets a numeric input (float) from the user with validation.

    Args:
        prompt (str): The message to display to the user.

    Returns:
        float: The validated numeric input.
    """
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:  # Ensure non-negative input
                return value
            else:
                print("Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    """
    Main function to calculate and display the width of a rectangle.
    """
    print("Welcome to the Rectangle Dimension Calculator!")
    unit = input("What is your measurement unit (in., ft., cm., etc.)? ")

    area = get_numeric_input(f"What is the area of the rectangle in square {unit}? ")
    length = get_numeric_input(f"What is the length of the rectangle in {unit}? ")

    try:
        width = area / length
        print(f"Your rectangle is {width:.2f} {unit} wide.")
    except ZeroDivisionError:
        print("Error: Length cannot be zero.")
    except Exception as e:  # Catch any other unexpected exception
        print(f"An unexpected error occurred: {e}")

main()
