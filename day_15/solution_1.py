from time import sleep

input = open("./day_15/input.txt", "r").read()

map, moves = input.split("\n\n")

map = [list(line) for line in map.splitlines()]
moves = moves.replace('\n', '')

N = len(map)
M = len(map[0])

# (dy, dx)
directions = {
    "^": (-1,0),
    ">": (0,1),
    "<": (0,-1),
    "v": (1,0)
}

def find_start():
    for i in range(N):
        for j in range(M):
            if map[i][j] == "@":
                map[i][j] = "."
                return (i,j)
            
y,x = find_start()

move_counter = 0
def draw_map(move, y, x):
    global move_counter
    print(f"===== MOVE {move} ({move_counter}/{len(moves)}) =====")
    move_counter += 1
    for i in range(N):
        line_copy = map[i].copy()
        if i == y:
            line_copy[x] = "@"
        print("".join(line_copy))
    sleep(0.1)

prev_move = "START"
for move in moves:
    draw_map(prev_move, y, x)
    prev_move = move
    dy,dx = directions[move]
    ny, nx = y + dy, x + dx
    if map[ny][nx] == "#":
        continue
    
    if map[ny][nx] == ".":
        y, x = ny, nx
        continue

    # if map[ny][nx] == "O"
    while True:
        ny, nx = ny + dy, nx + dx
        if map[ny][nx] == "#":
            break
        if map[ny][nx] == "O":
            continue

        # if map[ny][nx] == "."
        map[ny][nx] = "O"
        y, x = y + dy, x + dx
        map[y][x] = "."
        break

GPS_cords_sum = 0
for i in range(N):
    for j in range(M):
        if map[i][j] == "O":
            GPS_cords_sum += 100 * i + j

print(GPS_cords_sum)