import re

with open("day_3/input.txt") as file:
    input = "".join(file)

pattern = "mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)"
commands = re.findall(pattern, input)
multiplications_result = 0
operations_enabled = True
for command in commands:
    if "do()" in command:
        operations_enabled = True
    elif "don't()" in command:
        operations_enabled = False
    else:
        numbers = command[4:-1]
        n1 = int(numbers.split(',')[0])
        n2 = int(numbers.split(',')[1])
        multiplications_result += n1 * n2 * operations_enabled

print(multiplications_result)