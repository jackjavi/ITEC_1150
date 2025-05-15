"""
Author: Yusuf Hassan
Date: 2025-01-28
Description: This program calculates and displays the total amount spent on bus fares
        for the month, including regular and rush hour fares.
"""

# Define variables for fare rates and rides
regular_fare = 1.75
rush_hour_fare = 3.00
regular_rides = 7
rush_hour_rides = 12

# Calculate total spending
regular_fare_total = regular_fare * regular_rides
rush_hour_fare_total = rush_hour_fare * rush_hour_rides
total_spent = regular_fare_total + rush_hour_fare_total

# Round the total spent to two decimal places
total_spent_rounded = round(total_spent, 2)

# Display the total spending with a meaningful message
print(f"I spent ${total_spent_rounded:.2f} this month on bus fare.")
