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
    

    for i in range(len(antennas)):
        for j in range(i+1, len(antennas)):
            Ax, Ay = antennas[i]
            Bx, By = antennas[j]
            
            P1x = 2*Ax - Bx
            P1y = 2*Ay - By
            
            P2x = 2*Bx - Ax
            P2y = 2*By - Ay
            
            if 0 <= P1x < rows and 0 <= P1y < cols:
                antinode_positions.add((P1x, P1y))
            if 0 <= P2x < rows and 0 <= P2y < cols:
                antinode_positions.add((P2x, P2y))


print(len(antinode_positions))
