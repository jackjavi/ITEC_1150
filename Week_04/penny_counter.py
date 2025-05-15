"""
Author: Yusuf Hassan
Date: 2025-02-11
Description: This program asks the user for the number of pennies in a jar and provides
    a message indicating whether they have less than, more than, or exactly
    one dollar. It then tells the user the exact value of their pennies in
    dollars and cents.
"""

pennies_str = input("How many pennies do you have in your jar? ")

if pennies_str.isnumeric():
    pennies = int(pennies_str)

    if pennies >= 0:  # Ensure non-negative
        if pennies < 100:
            print("You have less than a dollar.")
        elif pennies > 100:
            print("You have more than a dollar.")
        else:
            print("You have exactly one dollar.")

        dollars = pennies // 100  # Integer division to get the number of dollars
        cents = pennies % 100   # Modulo to get the remaining cents

        print(f"You have ${dollars}.{cents:02} to be exact.")  # Format to 2 digits for cents

    else:
        print("Please enter a whole number greater than or equal to 0.")

else:
    print("Please enter a whole number greater than or equal to 0.")