"""
Author: Yusuf Hassan
Date: 2025-02-04
Description: This program asks the user for:
    - the no. of miles they drove on a trip
    - the no. of gallons of gas they used
    - the price of gas per gallon
calculates and displays the cost of the trip
& the miles per gallo (MPG) for the trip in the table format.
"""

# Get user input
miles_driven = float(input("Enter the no. of miles they drove: "))
gallons_used = float(input("Enter the no. of gallons of gas you used: "))
price_per_gallon = float(input("Enter the price of gas per gallon: "))

# Calculates miles per gallon (MPG)
mpg = round(miles_driven / gallons_used, 2)

# Calculates total trip cost
trip_cost = round(gallons_used * price_per_gallon, 2)

# Display results in table format
print("\nHere are some fun facts about your trip:")
print(f"{'MPG':<15} {mpg:>10.2f}")
print(f"{'Trip Cost':<15}$ {trip_cost:>9.2f}")
