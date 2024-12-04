import re

with open('day_3/test_input.txt', 'r') as f:
    data = f.read()

pattern = r'mul\((\d{1,3}),(\d{1,3})\)'

matches = re.findall(pattern, data)

total_sum = 0

for num1, num2 in matches:
    result = int(num1) * int(num2)
    total_sum += result

print(f"The total sum of the results is: {total_sum}")
