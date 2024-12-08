from itertools import cycle
input = open("./day_6/input.txt", "r").read()

map = input.split("\n")

N = len(map)
M = len(map[0])

def guard_in_area(x, y):
    return x >= 0 and x < M and y >= 0 and y < N

def find_start():
    for i in range(N):
        for j in range(M):
            if map[i][j] == "^":
                return (j,i)

# 90deg rotation clockwise 
# (0,-1) -> (1,0) -> (0,1) -> (-1,0)
directions = [(0,-1), (1,0), (0,1), (-1,0)]
directions_iterator = cycle(directions)
dx,dy = next(directions_iterator)
x,y = find_start()

visited_positions = set()
while guard_in_area(x,y):
    visited_positions.add((x,y))
    next_x, next_y = x + dx, y + dy
    if guard_in_area(next_x, next_y) and map[next_y][next_x] == "#":
        dx,dy = next(directions_iterator)
    x, y = x + dx, y + dy

print(len(visited_positions))
