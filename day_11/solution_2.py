input = open("./day_11/input.txt", "r").read()
numbers = {int(n):1 for n in input.split(" ")}

def blink(numbers):
    res = {}
    for n, count in numbers.items():
        if n == 0:
            res[1] = res.get(1, 0) + count
        elif len(str(n)) % 2 == 0:
            half_index = len(str(n)) // 2
            t1 = int(str(n)[:half_index])
            res[t1] = res.get(t1, 0) + count
            t2 = int(str(n)[half_index:])
            res[t2] = res.get(t2, 0) + count
        else:
            t = n * 2024
            res[t] = res.get(t, 0) + count
    return res

for i in range(75):
    numbers = blink(numbers)

stones_count = sum([c for _,c in numbers.items()])
print(stones_count)