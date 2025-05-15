"""
Author: Yusuf Hassan
Date: 2025-01-25
Description: Use format method to format string
"""
user = "Yusuf"
age = 12
print('My name is {} and I\'m {}'.format(user, age))
print(f'My name is {user} and I\'m {age}')
print('My name is %s and I\'m %d' % (user, age))

# two columns table using a "leader" character
city = 'New York'
temp = 56
chance_precip = 40
parking = 20.00
guests = 1000
salary = 54321
print(f'Welcome!\n{city} Hilton Today')
print('{:.<18}{:.>5d}f'.format('Temperature', temp))
print('{:.<18}{:.>5.2f}f'.format('Parking', parking))
print(f'{"Salary":.<13}${salary:>7,.3f}')

name1 = input('Please type your name here: ')
print(f'Hello {name1}')