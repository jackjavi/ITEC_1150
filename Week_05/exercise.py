"""
Author: Yusuf Hassan
Date: 2025-02-18
Description:
"""
print('Here is the 12 times table:')
for number in range(13):
    print(f'\t{number:>2d} times 12 is {number * 12:>3d}')


my_college = 'Minneapolis'
for letter in my_college:
    print(letter)
print('Acronym = ' + my_college[0] + 'C')


print('I can print and add up all the numbers between 50 and 100.')
total = 0
for number in range(50, 100):
    print(number)
    total += number
print(f'The total is: {total:,d}.')


while True:
    print('Welcome to the coffee shop.')
    total = 0.0
    items = int(input('How many items is the customer buying?: '))
    for item in range(items):
        price = float(input('Enter price in whole dollars for item #{}?: '.format(item+1)))
        total = total + price
        print(f'Running subtotal = ${total:.2f}')
    print(f'Grand total = ${total:.2f}')
    close = input('Time to close? Enter y or n:')
    if close == 'y':
        break
print('Thank you for shopping!')