"""
Author: Yusuf Hassan
Date: 2025-01-28
Description: This program calculates and displays the total weekly gross pay,
        including both regular and overtime pay, rounded to two decimal places.
"""

# Define variables
regular_hours = 40
overtime_hours = 10
regular_wage = 15.34
overtime_rate = 1.5  # 1.5 times the regular wage

# Calculate regular and overtime pay
regular_pay = regular_hours * regular_wage
overtime_pay = overtime_hours * (regular_wage * overtime_rate)

# Calculate total gross pay
gross_pay = regular_pay + overtime_pay

# Round the gross pay to two decimal places
gross_pay_rounded = round(gross_pay, 2)

# Display the gross pay with proper formatting
print(f"Your gross pay is ${gross_pay_rounded:.2f}")
