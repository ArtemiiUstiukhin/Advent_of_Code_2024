input = open("./day_4/input.txt", "r").read()
data = input.split('\n')

word = "XMAS"
N = len(data)
M = len(data[0])

search_directions = [ -1, 0, 1 ]

def try_find_xmas(x, y, dx, dy):
    for i in range(len(word)):
        xi = x + i * dx
        yi = y + i * dy
        if xi < 0 or xi >= M or yi < 0 or yi >= N:
            return False
        if data[yi][xi] != word[i]:
            return False
    return True

xmas_counter = 0
for i in range(N):
    for j in range(M):
        if data[i][j] != "X":
            continue
        for dy in search_directions:
            for dx in search_directions:
                if dx == dy == 0:
                    continue
                xmas_counter += try_find_xmas(j, i, dx, dy)

print(xmas_counter)