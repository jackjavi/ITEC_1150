"""
Author: Yusuf Hassan
Date: 2025-04-01
Description: This program takes a title from the user, formats it to title case, and displays the result.
"""

def main():
    """
    Main function to get input, validate, call processing, and display the result.
    """
    print("Welcome to the title validation program.")
    while True:
        title = input("Please enter a title for validation & correction: ").strip()
        if title:  # Check if the title is not blank
            break
        else:
            print("Please try again to enter a title: ")

    formatted_title = processing(title)
    print("The corrected title is", formatted_title)
    print("Thanks for using the program.")

def processing(title):
    """
    Formats the given title to title case using a loop instead of .join().

    Args:
        title (str): The title to format.

    Returns:
        str: The formatted title.
    """
    words = title.split()
    formatted_words = []
    lowercase_words = ["the", "a", "an", "of"]

    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1 or word.lower() not in lowercase_words:
            formatted_words.append(word.capitalize())
        else:
            formatted_words.append(word.lower())

    formatted_title = ""  # Initialize an empty string
    for i, word in enumerate(formatted_words):
        formatted_title += word
        if i < len(formatted_words) - 1:  # Add space if not the last word
            formatted_title += " "

    return formatted_title

if __name__ == "__main__":
    main()