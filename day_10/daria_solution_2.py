with open('day_10/test_input.txt', 'r') as f:
    grid = [line.strip() for line in f]

rows = len(grid)
cols = len(grid[0]) if rows > 0 else 0

heights = [[int(ch) for ch in row] for row in grid]

directions = [(1,0), (-1,0), (0,1), (0,-1)]

def neighbors(r, c):
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            yield nr, nc

dp = [[0]*(cols) for _ in range(rows)]


for r in range(rows):
    for c in range(cols):
        if heights[r][c] == 9:
            dp[r][c] = 1

for h in range(8, -1, -1):
    for r in range(rows):
        for c in range(cols):
            if heights[r][c] == h:
                total_paths = 0
                for nr, nc in neighbors(r, c):
                    if heights[nr][nc] == h + 1:
                        total_paths += dp[nr][nc]
                dp[r][c] = total_paths

total_rating = 0
for r in range(rows):
    for c in range(cols):
        if heights[r][c] == 0:
            total_rating += dp[r][c]

print(total_rating)
