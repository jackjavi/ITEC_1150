import re
phone_regex = re.compile(r'\d{3}-\d{3}-\d{4}')
source1 = phone_regex.search('My number is 415-555-4242.')
source2 = phone_regex.search('My number is 415-555-4242. 415-555-4242')
print(source1)
print(source2)
print(source1.group())
print(source2.group())