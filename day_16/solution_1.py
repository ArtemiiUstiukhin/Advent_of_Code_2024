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
    if score >= ex_score or score >= end_score:
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

lowest_score = min(maze.get((1,M-2,-1,0), float('inf')), maze.get((1,M-2,0,1), float('inf')))
print(lowest_score)