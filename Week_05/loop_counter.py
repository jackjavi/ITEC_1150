"""
Author: Yusuf Hassan
Date: 2025-02-18
Description: This program demonstrates various counting loops as specified in the lab instructions.
"""

print("Here are the numbers from 0 through 5:")
for number in range(6):  # range(6) generates numbers from 0 to 5
    print(number)

print("\nHere are the numbers from 1 through 20:")
for number in range(1, 21):  # range(1, 21) generates numbers from 1 to 20
    print(number)

print("\nHere are the even numbers from 0 through 24:")
for number in range(0, 25, 2):  # range(0, 25, 2) generates even numbers from 0 to 24
    print(number)

print("\nHere are the odd numbers from 37 through 53:")
for number in range(37, 54, 2):  # range(37, 54, 2) generates odd numbers from 37 to 53
    print(number)

print("\nHere are the multiples of 10 from 10 through 60:")
for number in range(10, 61, 10):  # range(10, 61, 10) generates multiples of 10
    print(number)

print("\nHere is a countdown from 30 through 20:")
for number in range(30, 19, -1):  # range(30, 19, -1) counts down from 30 to 20
    print(number)