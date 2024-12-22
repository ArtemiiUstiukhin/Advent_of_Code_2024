import math

input = open("./day_14/input.txt", "r").read()
robots = input.splitlines()

N = 103
M = 101
seconds_elapsed = 100

zones = {
    (0,0): 0,
    (0,1): 0,
    (1,0): 0,
    (1,1): 0
}

for robot in robots:
    p,v = robot.split(" ")
    x,y = [int(n) for n in p[2:].split(",")]
    dx,dy = [int(n) for n in v[2:].split(",")]
    
    x = (x + dx * seconds_elapsed) % M
    y = (y + dy * seconds_elapsed) % N
        
    if (x == (M // 2)) or (y == (N // 2)):
        continue

    zones[( y // (N // 2 + 1)), ( x // (M // 2 + 1))] += 1

print(math.prod(zones.values()))