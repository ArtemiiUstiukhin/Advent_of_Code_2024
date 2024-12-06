with open('day_6/test_input.txt', 'r') as f:
    data = f.read()

lines = data.split('\n')


directions = ['^', '>', 'v', '<']

# guard's starting position and direction
start_x = start_y = 0
direction_index = 0
found = False
for i, line in enumerate(lines):
    for j, ch in enumerate(line):
        if ch in directions:
            start_x, start_y = i, j
            direction_index = directions.index(ch)
            found = True
            break
    if found:
        break

moves = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1)
}

visited = set()
visited.add((start_x, start_y))

x, y = start_x, start_y

while True:
    current_dir = directions[direction_index]
    dx, dy = moves[current_dir]
    front_x, front_y = x + dx, y + dy

    inside = 0 <= front_x < len(lines) and 0 <= front_y < len(lines[0])

    if inside and lines[front_x][front_y] == '#':
        direction_index = (direction_index + 1) % 4
    else:
        if not inside:
            break
        x, y = front_x, front_y
        visited.add((x, y))

print(len(visited))
