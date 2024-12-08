import math

with open('day_8/test_input.txt', 'r') as f:
    grid = [line.rstrip('\n') for line in f]

rows = len(grid)
cols = len(grid[0]) if rows > 0 else 0


frequency_map = {}
for x in range(rows):
    for y in range(cols):
        ch = grid[x][y]
        if ch.isalnum():
            if ch not in frequency_map:
                frequency_map[ch] = []
            frequency_map[ch].append((x, y))

antinode_positions = set()


for freq, antennas in frequency_map.items():
    if len(antennas) < 2:
        continue 

    lines = set()

    for i in range(len(antennas)):
        for j in range(i + 1, len(antennas)):
            x1, y1 = antennas[i]
            x2, y2 = antennas[j]

            dx = x2 - x1
            dy = y2 - y1

            if dx == 0 and dy == 0:
                continue  

            gcd_val = math.gcd(dx, dy)
            if gcd_val != 0:
                dx_norm = dx // gcd_val
                dy_norm = dy // gcd_val
            else:
                dx_norm, dy_norm = dx, dy


            if dx_norm < 0 or (dx_norm == 0 and dy_norm < 0):
                dx_norm *= -1
                dy_norm *= -1


            a = dy_norm
            b = -dx_norm
            c = dx_norm * y1 - dy_norm * x1

     
            gcd_abc = math.gcd(a, math.gcd(b, c))
            if gcd_abc != 0:
                a_norm = a // gcd_abc
                b_norm = b // gcd_abc
                c_norm = c // gcd_abc
            else:
                a_norm, b_norm, c_norm = a, b, c

            if a_norm < 0 or (a_norm == 0 and b_norm < 0):
                a_norm *= -1
                b_norm *= -1
                c_norm *= -1

            line = (a_norm, b_norm, c_norm)
            lines.add(line)

    for line in lines:
        a, b, c = line
        for x in range(rows):
            for y in range(cols):
                if a * x + b * y + c == 0:
                    antinode_positions.add((x, y))


print(len(antinode_positions))
