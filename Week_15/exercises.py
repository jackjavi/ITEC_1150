import csv
example_file = open('example1.csv', encoding = 'utf-8')
example_reader = csv.reader(example_file)
for row in example_reader:
    print('{:<18} {:^18} {:>5}'.format(*row, end = ''))