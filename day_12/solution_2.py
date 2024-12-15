from queue import Queue

input = open("./day_12/input.txt", "r").read()
map = input.splitlines()

N = len(map)
M = len(map[0])

# (dy, dx)
directions = [(-1,0), (0,-1), (1,0), (0,1)]

def in_map(x, y):
    return x >= 0 and x < M and y >= 0 and y < N

non_visited_garden_plots = set()
regions = []
for i in range(N):
    for j in range(M):
        non_visited_garden_plots.add((i,j))

# identify regions
while len(non_visited_garden_plots) > 0:
    plot = list(non_visited_garden_plots)[0]
    q = Queue()
    q.put(plot)
    region = set()
    i,j = plot
    plant_type = map[i][j]
    while not q.empty():
        plot = q.get()
        region.add(plot)
        non_visited_garden_plots.remove(plot)
        y,x = plot
        for dy,dx in directions:
            nx = x + dx
            ny = y + dy
            if in_map(nx, ny) and map[ny][nx] == plant_type and (ny,nx) in non_visited_garden_plots and (ny,nx) not in q.queue:
                q.put((ny,nx))
    regions.append(region)

def find_top_border(region):
    min_y = min([y for y,x in region])
    min_x = min([x for y,x in region if y == min_y])
    return min_y, min_x

def is_same_border(y, x, d_index, plant_type):
    dy,dx = directions[d_index]
    nx = x + dx
    ny = y + dy
    return not in_map(nx, ny) or map[ny][nx] != plant_type

def find_border_plots(region):
    border_plots = set()
    for y,x in region:
        for i in range(len(directions)):
            dy,dx = directions[i]
            if not (y + dy, x + dx) in region:
                # add plot cords + border direction index
                border_plots.add((y,x,i))
    return border_plots

total_price = 0
for region in regions:
    area = len(region)
    # find all border plots
    border_plots = find_border_plots(region)
    sides_count = 0
    while len(border_plots) > 0:
        y,x,d_index = list(border_plots)[0]
        plant_type = map[y][x]
        visited_border_plots = set()
        # go along each border clockwise
        while (y,x,d_index) not in visited_border_plots:
            visited_border_plots.add((y,x,d_index))
            # try continue along the same border side
            dy,dx = directions[(d_index - 1) % 4]
            nx = x + dx
            ny = y + dy
            if in_map(nx, ny) and map[ny][nx] == plant_type and is_same_border(ny, nx, d_index, plant_type):
                x = nx
                y = ny
                continue
            else: 
                # try turn left
                # check if the next plot along the same border side exists
                if in_map(nx, ny) and map[ny][nx] == plant_type:
                    dy,dx = directions[d_index]
                    nx = nx + dx
                    ny = ny + dy
                    # check if the next plot along the rotated clockwise border side exists
                    if in_map(nx, ny) and map[ny][nx] == plant_type and is_same_border(ny, nx, (d_index + 1) % 4, plant_type):
                        x = nx
                        y = ny
                        d_index = (d_index + 1) % 4
                        sides_count += 1
                        continue
                else: # turn right
                    d_index = (d_index - 1) % 4
                    sides_count += 1
                    continue
        # remove visited_border_plots
        border_plots.difference_update(visited_border_plots)
    # print(f"Plant: {plant_type}, sides_count: {sides_count}")
    total_price += sides_count * area
print(total_price)
