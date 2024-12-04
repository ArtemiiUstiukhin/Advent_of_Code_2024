import re

with open('day_3/test_input.txt', 'r') as f:
    data = f.read()

pattern = r"(?P<do>do\(\))|(?P<dont>don't\(\))|(?P<mul>mul\((?P<num1>\d{1,3}),(?P<num2>\d{1,3})\))"

mul_enabled = True
total_sum = 0

for match in re.finditer(pattern, data):
    if match.group('do'):
        mul_enabled = True
    elif match.group('dont'):
        mul_enabled = False
    elif match.group('mul'):
        if mul_enabled:
            num1 = int(match.group('num1'))
            num2 = int(match.group('num2'))
            result = num1 * num2
            total_sum += result

print(f"The total sum of the results is: {total_sum}")