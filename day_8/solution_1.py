from itertools import combinations

input = open("./day_8/input.txt", "r").read()
map = input.splitlines()

N = len(map)
M = len(map[0])

def get_antinode_single_dimention(v1, v2):
    diff_factor = 1 if v1 > v2 else -1
    return v1 + abs(v1 - v2) * diff_factor

def validate_antinode(cords):
    x,y = cords
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
        antinode_1 = (get_antinode_single_dimention(a1_x, a2_x), get_antinode_single_dimention(a1_y, a2_y))
        if validate_antinode(antinode_1):
            antinodes.add(antinode_1)
        antinode_2 = (get_antinode_single_dimention(a2_x, a1_x), get_antinode_single_dimention(a2_y, a1_y))
        if validate_antinode(antinode_2):
            antinodes.add(antinode_2)

print(len(antinodes))