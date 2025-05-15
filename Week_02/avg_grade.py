"""
Author: Yusuf Hassan
Date: 2025-01-28
Description: This program calculates and displays the average test score of three students,
        rounded to two decimal places.
"""

# Define variables
score1 = 45
score2 = 74
score3 = 63

# Calculate the average of the 3 scores
average_score = (score1 + score2 + score3) / 3.0

# Round the average to two decimal places
average_score_rounded = round(average_score, 2)

# Display the average with proper formatting
print(f"The average test score is {average_score_rounded:.2f}")
