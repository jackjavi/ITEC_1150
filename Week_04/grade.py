"""
Author: Yusuf Hassan
Date: 2025-02-11
Description: This program asks the user for a quiz score (0-100) and displays the
    corresponding letter grade with feedback. It validates the input to
    ensure it is a number.
"""

score_str = input('Enter quiz score - whole number 0-100: ')

if score_str.isnumeric():
    score = int(score_str)

    if 0 <= score <= 100:  # Check if in range only if it's a number
        # Determine the letter grade and feedback
        if score >= 90:
            grade = 'A'
            feedback = 'Excellent work!'
        elif score >= 80:
            grade = 'B'
            feedback = 'Good job!'
        elif score >= 70:
            grade = 'C'
            feedback = 'Remember you can resubmit for full points!'
        elif score >= 60:
            grade = 'D'
            feedback = 'Please contact the instructor for help.'
        else:
            grade = 'F'
            feedback = 'See the instructor during office hours for assistance.'

        # Display the results
        print(f'Grade: {grade}')
        print('Hello{:<20'.format(feedback))
    else:
        print('Score must be between 0 and 100.')  # Range error message

else:
    print('Invalid input. Please enter a whole number.')  # Non-numeric error message