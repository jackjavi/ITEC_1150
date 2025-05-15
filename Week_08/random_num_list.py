"""
Author: Yusuf Hassan
Date: 2025-03-18
Description: This program generates a list of random integers, sorts it, and displays various statistics.
"""

import random

def get_positive_int():
    """Gets a positive integer from the user with validation."""
    while True:
        try:
            num = int(input("Please enter how many random numbers you'd like to generate: "))
            if num > 0:
                return num
            else:
                print("Enter a whole number greater than 0: ")
        except ValueError:
            print("Please enter a whole number: ")

def generate_random_list(count):
    """Generates a list of random integers between 1 and 100."""
    num_list = []
    for _ in range(count):
        num_list.append(random.randrange(1, 101))
    return num_list

def display_list_info(num_list):
    """Displays the sorted list, total, min, and max values."""
    sorted_list = sorted(num_list)  # Sort the list
    print(f"Here is your list of {len(sorted_list)} integers, randomly selected and sorted:")
    print(sorted_list)

    print("\nHere is your list, printed with the shortcut method:")
    print(*sorted_list, sep=", ")

    print("\nHere is your list, printed via a loop, with total:")
    total = sum(sorted_list)
    for i in range(len(sorted_list)):
        print(sorted_list[i], end="")
        if i < len(sorted_list) - 1:
            print(" + ", end="")
    print(" =", total)

    min_val = min(sorted_list)
    max_val = max(sorted_list)
    print(f"\nThe minimum is {min_val} and the maximum is {max_val}.")

def main():
    count = get_positive_int()
    num_list = generate_random_list(count)
    display_list_info(num_list)

main()