"""
Author: Yusuf Hassan
Date: 2025-02-25
Description: This program asks the user for two numbers (small and large),
    then prints the numbers between them (inclusive) and their sum.
    It uses functions for input validation.
"""

def get_int_input_minimum(minimum):
    while True:
        value_str = input(f"Please enter a whole number greater than {minimum}: ")
        if value_str.isnumeric():
            value = int(value_str)
            if value > minimum:
                return value
            else:
                print(f"Please enter a whole number greater than {minimum}.")
        else:
            print("Please enter a whole number only.")

def main():
    print("Welcome to our counting program.")
    print("(It also adds up the digits counted!)")

    small_num = get_int_input_minimum(-1)  # Allow any number greater than -1 (i.e., 0 or higher)
    large_num = get_int_input_minimum(small_num)

    total = 0
    for num in range(small_num, large_num + 1):
        print(num)
        total += num

    print(f"The total of all the counted numbers is {total}.")

main()