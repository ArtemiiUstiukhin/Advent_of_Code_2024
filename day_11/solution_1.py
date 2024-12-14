input = open("./day_11/test_input.txt", "r").read()
numbers = [int(n) for n in input.split(" ")]

def blink(numbers):
    res = []
    for n in numbers:
        if n == 0:
            res.append(1)
        elif len(str(n)) % 2 == 0:
            half_index = len(str(n)) // 2
            res.append(int(str(n)[:half_index]))
            res.append(int(str(n)[half_index:]))
        else:
            res.append(n * 2024)
    return res

for i in range(75):
    print(f'blink {i}: {len(set(numbers))}/{len(numbers)}')
    numbers = blink(numbers)

print(len(numbers))