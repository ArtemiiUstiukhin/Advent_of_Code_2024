from queue import Queue

input = open("./day_16/input.txt", "r").read()

map = input.splitlines()

N = len(map)
M = len(map[0])

# (dy, dx)
turn_right = {
    (0,-1): (-1,0),
    (-1,0): (0,1),
    (0,1): (1,0),
    (1,0): (0,-1)
}
turn_left = {
    (0,1): (-1,0),
    (-1,0): (0,-1),
    (0,-1): (1,0),
    (1,0): (0,1)
}

maze = {}
route = Queue()
route.put((N-2,1,0,1,0))
while not route.empty():
    y,x,dy,dx,score = route.get()
    ex_score = maze.get((y,x,dy,dx), float('inf'))
    end_score = min(maze.get((1,M-2,-1,0), float('inf')), maze.get((1,M-2,0,1), float('inf')))
    if score > ex_score or score >= end_score:
        continue
    
    maze[y,x,dy,dx] = score

    # try go straight
    if map[y+dy][x+dx] != "#":
        route.put((y+dy,x+dx,dy,dx,score+1))

    # try turn right
    dry,drx = turn_right[(dy,dx)]
    if map[y+dry][x+drx] != "#":
        route.put((y+dry,x+drx,dry,drx,score+1001))

    # try turn left
    dly,dlx = turn_left[(dy,dx)]
    if map[y+dly][x+dlx] != "#":
        route.put((y+dly,x+dlx,dly,dlx,score+1001))

oposite_direction = {
    (0,1): (0,-1),
    (0,-1): (0,1),
    (1,0): (-1,0),
    (-1,0): (1,0)
}

best_paths = set()
route = Queue()
route.put((1,M-2,1,0))
while not route.empty():
    y,x,dy,dx = route.get()
    if (y,x,-dy,-dx) not in maze:
        continue

    score = maze[(y,x,-dy,-dx)]
    best_paths.add((y,x))

    for ddx,ddy in [(dy,dx), turn_right[(dy,dx)], turn_left[(dy,dx)]]:
        if map[y+ddy][x+ddx] != "#":
            straight_score = maze.get((y+ddy,x+ddx,-ddy,-ddx), float('inf'))
            if score - straight_score == 1:
                route.put((y+ddy,x+ddx,ddy,ddx))

            dry,drx = turn_right[(ddy,ddx)]
            right_score = maze.get((y+ddy,x+ddx,-dry,-drx), float('inf'))
            if score - right_score == 1001:
                route.put((y+ddy,x+ddx,dry,drx))

            dly,dlx = turn_left[(ddy,ddx)]
            left_score = maze.get((y+ddy,x+ddx,-dly,-dlx), float('inf'))
            if score - left_score == 1001:
                route.put((y+ddy,x+ddx,dly,dlx))
    
# def draw_map():
#     for i in range(N):
#         line = []
#         for j in range(M):
#             line.append("O" if (i,j) in best_paths else map[i][j])
#         print("".join(line))

# draw_map()

print(len(best_paths))