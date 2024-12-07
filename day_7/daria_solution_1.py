from itertools import product

with open('day_7/test_input.txt', 'r') as f:
    data = f.read().strip()

lines = data.split('\n')
total_sum = 0

for line in lines:
    parts = line.split(':')
    target = int(parts[0].strip())
    nums = list(map(int, parts[1].strip().split()))

    
    found_solution = False
    for ops in product(['+', '*'], repeat=len(nums)-1):
        value = nums[0]
        for op, n in zip(ops, nums[1:]):
            if op == '+':
                value = value + n
            else:
                value = value * n

        if value == target:
            found_solution = True
            break
    
    if found_solution:
        total_sum += target

print(total_sum)
