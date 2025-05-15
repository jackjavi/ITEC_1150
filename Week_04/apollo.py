"""
Author: Yusuf Hassan
Date: 2025-02-11
Description: Asks the user what year Apollo 11 landed on the moon and provides
    feedback based on their answer.
"""

year_str = input('What year did Apollo 11 land on the moon? ')

if year_str.isnumeric():  # Check if input is a number
    year = int(year_str)

    if year == 1969:
        print(f'Correct! {year} is the right answer!')
    elif year == 1968 or year == 1970:
        print(f'Close! Apollo 11 landed on the moon in 1969. Your guess of {year} was close, but wrong.')
    else:
        print(f'Sorry, {year} is the wrong answer. Apollo 11 landed on the moon in 1969.')

else:
    print("Invalid input. Please enter a year (a whole number).")