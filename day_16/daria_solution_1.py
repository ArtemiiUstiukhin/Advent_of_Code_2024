import heapq

with open("day_16/test_input.txt") as f:
    grid = [list(line.rstrip("\n")) for line in f]

rows = len(grid)
cols = len(grid[0])
start = None
end = None
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "S":
            start = (r, c)
        elif grid[r][c] == "E":
            end = (r, c)

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

dist = {}
start_state = (start[0], start[1], 1)
dist[start_state] = 0
priority_queue = [(0, start_state)]

while priority_queue:
    d, (r, c, dir) = heapq.heappop(priority_queue)
    if d > dist[(r, c, dir)]:
        continue
    if (r, c) == end:
        print(d)
        break

    left_dir = (dir - 1) % 4
    nd = d + 1000
    if (r, c, left_dir) not in dist or dist[(r, c, left_dir)] > nd:
        dist[(r, c, left_dir)] = nd
        heapq.heappush(priority_queue, (nd, (r, c, left_dir)))

    right_dir = (dir + 1) % 4
    nd = d + 1000
    if (r, c, right_dir) not in dist or dist[(r, c, right_dir)] > nd:
        dist[(r, c, right_dir)] = nd
        heapq.heappush(priority_queue, (nd, (r, c, right_dir)))

    nr, nc = r + dr[dir], c + dc[dir]
    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != "#":
        nd = d + 1
        if (nr, nc, dir) not in dist or dist[(nr, nc, dir)] > nd:
            dist[(nr, nc, dir)] = nd
            heapq.heappush(priority_queue, (nd, (nr, nc, dir)))
