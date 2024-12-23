from time import sleep

input = open("./day_15/input.txt", "r").read()

map_raw, moves = input.split("\n\n")

original_map = map_raw.splitlines()
map = []
# If the tile is #, the new map contains ## instead.
# If the tile is O, the new map contains [] instead.
# If the tile is ., the new map contains .. instead.
# If the tile is @, the new map contains @. instead.
for line in original_map:
    line = line.replace('#', '##')
    line = line.replace('O', '[]')
    line = line.replace('.', '..')
    line = line.replace('@', '@.')
    map.append(list(line))

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

def try_move_box(x1,x2,y,dy,boxes):
    if (y,x1) in boxes:
        return True
    boxes.add((y,x1))
    ny = y + dy
    if map[ny][x1] == "#" or map[ny][x2] == "#":
        return False
    if map[ny][x1] == "." and map[ny][x2] == ".":
        return True
    if map[ny][x1] == "[" or map[ny][x2] == "]":
        return try_move_box(x1, x2, ny, dy, boxes)
    left = (try_move_box(x1-1, x1, ny, dy, boxes) if map[ny][x1] == "]" else True)
    right = (try_move_box(x2, x2+1, ny, dy, boxes) if map[ny][x2] == "[" else True)
    return left and right

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
    sleep(0.05)

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

    if move == ">" or move == "<":
        while True:
            ny, nx = ny + dy, nx + 2*dx
            if map[ny][nx] == "#":
                break
            if map[ny][nx] == "[" or map[ny][nx] == "]":
                continue
                
            for j in range(abs(nx - x)-1):
                map[ny][nx - dx*j] = map[ny][nx - dx*(j+1)]
                
            
            map[ny][nx - dx*(abs(nx - x)-1)] = "."
            y, x = y + dy, x + dx
            break
    else:
        if map[ny][nx] == "[":
            nx1, nx2 = nx, nx+1
        else: 
            nx1, nx2 = nx-1, nx
        
         # if map[ny][nx] == "."
        boxes = set()
        res = try_move_box(nx1,nx2,ny,dy,boxes)
        if res:
            sorted_boxes = sorted(boxes, key=lambda cords: cords[0], reverse=(dy == 1))
            for (by,bx1) in sorted_boxes:
                map[by+dy][bx1] = "["
                map[by+dy][bx1+1] = "]"
                map[by][bx1] = "."
                map[by][bx1+1] = "."
            y, x = y + dy, x + dx
    
draw_map(prev_move, y, x)

GPS_cords_sum = 0
for i in range(N):
    for j in range(M):
        if map[i][j] == "[":
            GPS_cords_sum += 100 * i + j

print(GPS_cords_sum)