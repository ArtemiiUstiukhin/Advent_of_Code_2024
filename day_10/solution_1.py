from queue import Queue

input = open("./day_10/input.txt", "r").read()
map = input.splitlines()

N = len(map)
M = len(map[0])
directions = [(0,-1), (1,0), (0,1), (-1,0)]
trailheads = set()
tops = set()

for i in range(N):
    for j in range(M):
        if map[i][j] == "0":
            trailheads.add((i,j))
        elif map[i][j] == "9":
            tops.add((i,j))

def in_map(x, y):
    return x >= 0 and x < M and y >= 0 and y < N

def is_desc(x, y, nx, ny):
    return int(map[y][x]) - int(map[ny][nx]) == 1 

total_top_score = 0
for top in tops:
    top_score = 0
    routes = Queue()
    routes.put(top)
    visited_nodes = set()
    while not routes.empty():
        step = routes.get()
        if step in visited_nodes:
            continue
        visited_nodes.add(step)
        y,x = step
        if step in trailheads:
            top_score += 1
            continue
        for dy,dx in directions:
            ny = y + dy
            nx = x + dx
            if in_map(nx, ny) and is_desc(x,y,nx,ny):
                routes.put((ny,nx))
    total_top_score += top_score

print(total_top_score)