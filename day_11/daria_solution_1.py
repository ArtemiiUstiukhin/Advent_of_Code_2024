with open("test_input.txt", "r") as f:
    line = f.read().strip()
    stones_arrangement = [int(s) for s in line.split()]


def blink(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        else:
            s = str(stone)
            length = len(s)
            if length % 2 == 0:
                half = length // 2
                left_part = s[:half]
                right_part = s[half:]
                left_num = int(left_part)
                right_num = int(right_part)
                new_stones.append(left_num)
                new_stones.append(right_num)
            else:
                new_stones.append(stone * 2024)
    return new_stones


for _ in range(25):
    stones_arrangement = blink(stones_arrangement)

print(len(stones_arrangement))
