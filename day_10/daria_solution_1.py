from collections import deque

with open('day_10/test_input.txt', 'r') as f:
    grid = [line.strip() for line in f]

rows = len(grid)
cols = len(grid[0]) if rows > 0 else 0

heights = [[int(ch) for ch in row] for row in grid]

directions = [(1,0), (-1,0), (0,1), (0,-1)]

trailheads = []
for r in range(rows):
    for c in range(cols):
        if heights[r][c] == 0:
            trailheads.append((r, c))

def neighbors(r, c):
    for dr, dc in directions:
        nr, nc = r+dr, c+dc
        if 0 <= nr < rows and 0 <= nc < cols:
            yield nr, nc


def find_reachable_nines(start_r, start_c):
    visited = set()
    visited.add((start_r, start_c))
    queue = deque([(start_r, start_c)])
    reachable_nines = set()

    while queue:
        r, c = queue.popleft()
        current_h = heights[r][c]
        if current_h == 9:
            reachable_nines.add((r, c))
            continue
        next_h = current_h + 1
        for nr, nc in neighbors(r, c):
            if (nr, nc) not in visited and heights[nr][nc] == next_h:
                visited.add((nr, nc))
                queue.append((nr, nc))
    return len(reachable_nines)

total_score = 0
for (r, c) in trailheads:
    score = find_reachable_nines(r, c)
    total_score += score

print(total_score)
