with open("day_15/test_input.txt") as f:
    lines = [l.rstrip("\n") for l in f]

blank_index = lines.index("")
map_lines = lines[:blank_index]
move_lines = lines[blank_index + 1 :]
moves_str = "".join(move_lines)

rows = len(map_lines)
cols = len(map_lines[0])

grid = [list(row) for row in map_lines]

robot_r, robot_c = None, None
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "@":
            robot_r, robot_c = r, c
            break
    if robot_r is not None:
        break

directions = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}


def can_push(r, c, dr, dc):
    if grid[r][c] != "O":
        return True
    nr, nc = r + dr, c + dc
    if grid[nr][nc] == "#":
        return False
    if grid[nr][nc] == "O":
        if not can_push(nr, nc, dr, dc):
            return False
    return True


def do_push(r, c, dr, dc):
    if grid[r][c] != "O":
        return
    nr, nc = r + dr, c + dc
    if grid[nr][nc] == "O":
        do_push(nr, nc, dr, dc)
    grid[nr][nc] = "O"
    grid[r][c] = "."


for move in moves_str:
    dr, dc = directions[move]
    nr, nc = robot_r + dr, robot_c + dc
    if grid[nr][nc] == "#":
        continue
    if grid[nr][nc] == "O":
        if not can_push(nr, nc, dr, dc):
            continue
        do_push(nr, nc, dr, dc)
    grid[robot_r][robot_c] = "."
    grid[nr][nc] = "@"
    robot_r, robot_c = nr, nc

sum_gps = 0
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "O":
            sum_gps += 100 * r + c

print(sum_gps)
