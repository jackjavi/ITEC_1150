"""
Author: Yusuf Hassan
Date: 2025-04-08
Description: Prompts the user for a number and validates if it's a valid float using regex.
"""
import re

def main():
    """
    Prompts the user for a number and validates it.
    """
    number_input = input("Enter a number. Negatives and decimals are allowed: ").strip()
    if is_valid_float(number_input):
        print(f"{number_input} is a valid number!")
    else:
        print(f"{number_input} does not look like a valid number.")

def is_valid_float(number):
    """
    Checks if the given string is a valid float using regular expressions.

    Args:
        number (str): The string to validate.

    Returns:
        bool: True if the string is a valid float, False otherwise.
    """
    pattern = r"^-?\d+(\.\d+)?$"
    return re.match(pattern, number) is not None

if __name__ == "__main__":
    main()