"""
Author: Yusuf Hassan
Date: 2025-04-08
Description: Asks the user for a full name (first middle last) and uses regex to validate it.
"""
import re

def main():
    """
    Gets a full name from the user and validates it using regular expressions.
    """
    full_name_input = input("Enter a full name in the format 'first middle last': ").strip()
    if is_valid_full_name(full_name_input):
        capitalized_name = ' '.join(name.capitalize() for name in full_name_input.split())
        print(f"Here is the name: {capitalized_name}")
    else:
        print("This does not look like a name.")

def is_valid_full_name(name):
    """
    Checks if the given string could be a full name (three space-separated words with letters).

    Args:
        name (str): The string to validate.

    Returns:
        bool: True if the string could be a full name, False otherwise.
    """
    # Regex to check for three words with only letters, separated by spaces,
    # and ensuring the whole string matches from beginning to end.
    pattern = r"^[a-zA-Z]+ [a-zA-Z]+ [a-zA-Z]+$"
    return re.match(pattern, name) is not None

if __name__ == "__main__":
    main()