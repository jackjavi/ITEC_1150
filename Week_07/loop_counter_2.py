"""
Author: Yusuf Hassan
Date: 2025-03-04
Description: This program asks the user for two numbers (small and large),
  then prints the numbers between them (inclusive) and their sum.
  It uses functions for input validation and calculations.
"""

def main():
    """
    Main function to control the program flow.

    Handles the overall execution of the program, including:
        - Displaying welcome messages.
        - Getting the range of numbers from the user.
        - Processing the numbers to calculate the sum.
        - Displaying the total.
        - Asking the user if they want to restart the program.
        - Handling any exceptions that may occur.
    """
    try:
        print("Welcome to our counting program.")
        print("(It also adds up the digits counted!)")
        lower, upper = get_range_values()
        total = processing(lower, upper)
        display_total(total)
        restart = input("Do you want to run the program again? Enter y or n: ")
        if restart == 'y':
            main()
        else:
            print("Thanks for using the program!")
    except Exception as err:
        print(err)


def get_range_values():
    """
    Gets the lower and upper bounds of the range from the user.

    Returns:
        tuple: A tuple containing the lower and upper bounds (both integers).
    """
    lower = get_positive_int(0)  # Get the smaller number, minimum is 0
    upper = get_positive_int(lower + 1)  # Get the larger number, minimum is lower + 1
    return lower, upper


def processing(lower_val, upper_val):
    """
    Processes the numbers in the given range and calculates their sum.

    Args:
        lower_val (int): The lower bound of the range.
        upper_val (int): The upper bound of the range.

    Returns:
        int: The sum of the numbers in the range.
    """
    total = 0
    for num in range(lower_val, upper_val + 1):
        print(num)
        total += num
    return total


def display_total(total):
    """
    Displays the total sum of the numbers.

    Args:
        total (int): The total sum to be displayed.
    """
    print(f"The total of all the counted numbers is {total}.")


def get_positive_int(min_val):
    """
    This function is guaranteed to return an integer larger than min_val

    @param min_val: The minimum value to be accepted from the user
    @return: an integer > min_val
    """
    while True:
        try:
            value = int(input(f"Please enter a small number greater than or equal to {min_val}: "))
            if value < min_val:
                print(f"The value must be greater than {min_val}.")
            else:
                break
        except ValueError:
            print("Only digits are allowed.")
    return value


main()
