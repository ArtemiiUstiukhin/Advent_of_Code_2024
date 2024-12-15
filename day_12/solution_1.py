from queue import Queue

input = open("./day_12/test_input.txt", "r").read()
map = input.splitlines()

N = len(map)
M = len(map[0])
directions = [(0,-1), (1,0), (0,1), (-1,0)]

def in_map(x, y):
    return x >= 0 and x < M and y >= 0 and y < N

non_visited_garden_plots = set()
regions = []
for i in range(N):
    for j in range(M):
        non_visited_garden_plots.add((i,j))

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

total_price = 0
for region in regions:
    area = len(region)
    perimeter = 0
    for y,x in region:
        for dy,dx in directions:
            perimeter += not (y + dy, x + dx) in region
    total_price += perimeter * area

print(total_price)
