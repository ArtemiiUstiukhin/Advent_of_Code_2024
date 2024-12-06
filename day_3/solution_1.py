import re

with open("day_3/input.txt") as file:
    input = "".join(file)

pattern = "mul\(\d{1,3},\d{1,3}\)"
commands = re.findall(pattern, input)
multiplications_result = 0
for command in commands:
    numbers = command[4:-1]
    n1 = int(numbers.split(',')[0])
    n2 = int(numbers.split(',')[1])
    multiplications_result += n1 * n2

print(multiplications_result)