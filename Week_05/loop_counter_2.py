"""
Author: Yusuf Hassan
Date: 2025-02-18
Description: This program asks the user for two numbers (small and large),
    then prints the numbers between them (inclusive) and their sum.
"""

print("Welcome to our counting program..")
print("(It also adds up the digits counted!)")

while True:
    small_num_str = input("Please enter a small number, 0 or higher: ")
    if small_num_str.isnumeric():
        small_num = int(small_num_str)
        if small_num >= 0:
            break
        else:
            print("Please enter a whole number only, 0 or higher: ")
    else:
        print("Please enter a whole number only, 0 or higher: ")

while True:
    large_num_str = input(f"Please enter a whole number larger than {small_num}: ")
    if large_num_str.isnumeric():
        large_num = int(large_num_str)
        if large_num > small_num:
            break
        else:
            print(f"Please enter a whole number larger than {small_num}: ")
    else:
        print("Please enter a whole number only: ")

total = 0
for num in range(small_num, large_num + 1):
    print(num)
    total += num

print(f"The total of all the counted numbers is {total}.")