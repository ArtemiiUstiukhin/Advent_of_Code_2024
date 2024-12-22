input = open("./day_14/input.txt", "r").read()
robots_data = input.splitlines()
robots = {}

N = 103
M = 101
seconds_elapsed = 10_000

def draw_robots_map_small_resolution(k):
    robot_pos = set(robots.values())
    lines = []
    egg_found = False
    for i in range(N//2):
        line = []
        for j in range(M//2):
            line.append("X" if (2*j,2*i) in robot_pos or (2*j,2*i+1) in robot_pos or (2*j+1,2*i) in robot_pos or (2*j+1,2*i+1) in robot_pos else ".")
        print_line = "".join(line) + "\n"
        if "XXXXXXXXXXXXX" in print_line:
            print(f"Potential egg found after {k+1} sec elapsed!")
            egg_found = True
        lines.append(print_line)

    if egg_found:
        f = open("./day_14/output.txt", "a")
        f.write(f"===================\n")
        f.write(f"Seconds elapsed {k}\n")
        f.write(f"===================\n")
        for l in lines:
            f.write(l)
        f.close()
    
    return egg_found

for robot in robots_data:
    p,v = robot.split(" ")
    x,y = [int(n) for n in p[2:].split(",")]
    dx,dy = [int(n) for n in v[2:].split(",")]
    robots[(dx,dy)] = (x,y)

for k in range(seconds_elapsed):
    for (dx, dy), (x, y) in robots.items():
        robots[(dx, dy)] = ((x+dx)%M, (y+dy)%N)
    res = draw_robots_map_small_resolution(k)
