"""
Author: Yusuf Hassan
Date: 2025-04-22
Description: This program reads integers from ch_9_lab_data.txt,
             calculates their count, total, and average, and writes
             the summary to summary.txt in a formatted table.
"""

def main():
    data_file = 'ch_9_lab_data.txt'
    summary_file = 'summary.txt'
    numbers = []

    try:
        with open(data_file, 'r') as infile:
            for line in infile:
                try:
                    number = int(line.strip())
                    numbers.append(number)
                except ValueError:
                    print(f"Warning: Skipping non-integer value '{line.strip()}' in {data_file}")
    except FileNotFoundError:
        print(f"Error: The file '{data_file}' was not found.")
        return

    count = len(numbers)
    total = sum(numbers) if numbers else 0
    average = total / count if count > 0 else 0

    try:
        with open(summary_file, 'w') as outfile:
            outfile.write("{:<10} {:>10}\n".format("Count:", count))
            outfile.write("{:<10} {:>10}\n".format("Total:", total))
            outfile.write("{:<10} {:>10.2f}\n".format("Average:", average))
        print(f"Summary written to '{summary_file}'")
    except IOError:
        print(f"Error: Could not write to the file '{summary_file}'.")

if __name__ == "__main__":
    main()