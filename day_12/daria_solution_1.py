from collections import deque

with open("day_12/test_input.txt", "r") as f:
    grid = [line.rstrip("\n") for line in f]

rows = len(grid)
cols = len(grid[0]) if rows > 0 else 0

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visited = [[False] * cols for _ in range(rows)]


def bfs(start_r, start_c):
    letter = grid[start_r][start_c]
    queue = deque([(start_r, start_c)])
    visited[start_r][start_c] = True
    area = 0
    perimeter = 0

    while queue:
        r, c = queue.popleft()
        area += 1
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != letter:
                perimeter += 1
            else:
                if not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr, nc))
    return area, perimeter


total_price = 0
for r in range(rows):
    for c in range(cols):
        if not visited[r][c]:
            a, p = bfs(r, c)
            price = a * p
            total_price += price

print(total_price)
