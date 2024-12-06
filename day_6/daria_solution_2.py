with open('day_6/test_input.txt', 'r') as f:
    data = f.read()

lines = data.split('\n')

directions = ['^', '>', 'v', '<']
moves = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1)
}

start_x = start_y = 0
direction_index = 0
for i, line in enumerate(lines):
    for j, ch in enumerate(line):
        if ch in directions:
            start_x, start_y = i, j
            direction_index = directions.index(ch)
            break

rows = len(lines)
cols = len(lines[0])

def simulate(map_data):
    x, y = start_x, start_y
    dir_idx = direction_index

    visited_states = set()
    state = (x, y, dir_idx)

    while True:
        if state in visited_states:
            return (False, True)
        visited_states.add(state)

        current_dir = directions[dir_idx]
        dx, dy = moves[current_dir]
        front_x, front_y = x + dx, y + dy

        inside = 0 <= front_x < rows and 0 <= front_y < cols
        if inside:
            if map_data[front_x][front_y] == '#':
                dir_idx = (dir_idx + 1) % 4
            else:
                x, y = front_x, front_y
        else:
            return (True, False)

        state = (x, y, dir_idx)

def lines_to_list(lines):
    return [list(row) for row in lines]

def list_to_lines(lst):
    return [''.join(row) for row in lst]

original_map = lines_to_list(lines)

count_loop_positions = 0

for i in range(rows):
    for j in range(cols):
        if (i == start_x and j == start_y) or original_map[i][j] != '.':
            continue

        modified_map = [row[:] for row in original_map]
        modified_map[i][j] = '#'
        
        exited, looped = simulate(list_to_lines(modified_map))
        if looped:
            count_loop_positions += 1

print(count_loop_positions)
