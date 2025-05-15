"""
Author: Yusuf Hassan
Date: 2025-02-18
Description: This program calculates the average rainfall over a period of years.
    It uses nested loops to process data for each year and each month.
"""

num_years = int(input("How many years are in the rainfall sample? "))

total_rainfall_all_years = 0  # Initialize total rainfall for all years

for year in range(1, num_years + 1):
    print(f"Rainfall data for year #{year}:")
    total_rainfall_year = 0  # Initialize total rainfall for the current year

    for month in range(1, 13):
        rainfall = float(input(f"Enter rain for month #{month}: "))
        total_rainfall_year += rainfall

    average_monthly_rainfall_year = total_rainfall_year / 12
    print(f"Total rainfall for year #{year}: {total_rainfall_year:.2f}")
    print(f"Average monthly rainfall for year #{year}: {average_monthly_rainfall_year:.2f}")

    total_rainfall_all_years += total_rainfall_year  # Accumulate yearly totals

average_monthly_rainfall_all_years = total_rainfall_all_years / (num_years * 12)  # Calculate overall average

print(f"\nTotal rainfall, all years: {total_rainfall_all_years:.2f}")
print(f"Average monthly rainfall, all years: {average_monthly_rainfall_all_years:.2f}")