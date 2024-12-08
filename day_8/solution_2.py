from itertools import combinations

input = open("./day_8/input.txt", "r").read()
map = input.splitlines()

N = len(map)
M = len(map[0])

def get_antinode_delta(a1_x, a1_y, a2_x, a2_y):
    diff_factor_x = 1 if a1_x > a2_x else -1
    diff_factor_y = 1 if a1_y > a2_y else -1
    return (abs(a1_x - a2_x) * diff_factor_x, abs(a1_y - a2_y) * diff_factor_y)

def validate_antinode(x,y):
    return x >= 0 and x < M and y >= 0 and y < N

antenna_locations = {}
for i in range(N):
    for j in range(M):
        symbol = map[i][j]
        if symbol == ".":
            continue
        if symbol in antenna_locations:
            antenna_locations[symbol].append((j,i))
        else:
            antenna_locations[symbol] = [(j,i)]

antinodes = set()
for _, antenna_location in antenna_locations.items():
    if len(antenna_location) < 2:
        continue
    for a1, a2 in list(combinations(antenna_location, 2)):
        a1_x, a1_y = a1
        a2_x, a2_y = a2
        a1_dx, a1_dy = get_antinode_delta(a1_x, a1_y, a2_x, a2_y)
        a2_dx, a2_dy = get_antinode_delta(a2_x, a2_y, a1_x, a1_y)
        while validate_antinode(a1_x, a1_y):
            antinodes.add((a1_x, a1_y))
            a1_x += a1_dx
            a1_y += a1_dy
        while validate_antinode(a2_x, a2_y):
            antinodes.add((a2_x, a2_y))
            a2_x += a2_dx
            a2_y += a2_dy

print(len(antinodes))