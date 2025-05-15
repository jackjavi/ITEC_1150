"""
Author: Yusuf Hassan
Date: 2025-02-11
Description: This program asks the user for two colors from red, blue, or yellow.
    It then determines the resulting mixed color (purple, orange, or green)
    and reports it back to the user.  It handles invalid input.
"""

# Get the first color
color1 = input("Enter a primary color (red, blue, or yellow): ").lower()

if color1 == "red" or color1 == "blue" or color1 == "yellow":
    # Get the second color, ensuring it is different from the first
    if color1 == "red":
        color2 = input("Enter a different primary color (blue or yellow): ").lower()
        if color2 == "blue" or color2 == "yellow":
            # Determine the mixed color
            if color1 == color2:
                print("You cannot use the same primary colors.")

            elif (color1 == "red" and color2 == "blue") or \
                 (color1 == "blue" and color2 == "red"):
                print("Red and blue make purple.")

            elif (color1 == "red" and color2 == "yellow") or \
                 (color1 == "yellow" and color2 == "red"):
                print("Red and yellow make orange.")

        else:
            print("You can only choose blue or yellow")

    elif color1 == "blue":
        color2 = input("Enter a different primary color (red or yellow): ").lower()
        if color2 == "red" or color2 == "yellow":
            # Determine the mixed color
            if color1 == color2:
                print("You cannot use the same primary colors.")

            elif (color1 == "red" and color2 == "blue") or \
                 (color1 == "blue" and color2 == "red"):
                print("Red and blue make purple.")

            elif (color1 == "red" and color2 == "yellow") or \
                 (color1 == "yellow" and color2 == "red"):
                print("Red and yellow make orange.")

            elif (color1 == "blue" and color2 == "yellow") or \
                 (color1 == "yellow" and color2 == "blue"):
                print("Blue and yellow make green.")
        else:
            print("You can only choose red or yellow")

    elif color1 == "yellow":
        color2 = input("Enter a different primary color (red or blue): ").lower()
        if color2 == "red" or color2 == "blue":
            # Determine the mixed color
            if color1 == color2:
                print("You cannot use the same primary colors.")

            elif (color1 == "red" and color2 == "blue") or \
                 (color1 == "blue" and color2 == "red"):
                print("Red and blue make purple.")

            elif (color1 == "red" and color2 == "yellow") or \
                 (color1 == "yellow" and color2 == "red"):
                print("Red and yellow make orange.")

            elif (color1 == "blue" and color2 == "yellow") or \
                 (color1 == "yellow" and color2 == "blue"):
                print("Blue and yellow make green.")
        else:
            print("You can only choose red or blue")

else:
    print("You can only choose 'red', 'blue' or 'yellow'")