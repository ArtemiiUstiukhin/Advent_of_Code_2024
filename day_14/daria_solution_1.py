with open("day_14/test_input.txt") as f:
    lines = f.read().strip().split('\n')

robots = []
for line in lines:
    part_p, part_v = line.split(' ')
    px, py = map(int, part_p.split('=')[1].split(','))
    vx, vy = map(int, part_v.split('=')[1].split(','))
    robots.append((px, py, vx, vy))

W, H = 101, 103
for i, (px, py, vx, vy) in enumerate(robots):
    nx = (px + vx*100) % W
    ny = (py + vy*100) % H
    robots[i] = (nx, ny)


q1 = q2 = q3 = q4 = 0

for (x,y) in robots:
    if x == 50 or y == 51:
        continue
    if x<50 and y<51:
        q1+=1
    elif x>50 and y<51:
        q2+=1
    elif x<50 and y>51:
        q3+=1
    elif x>50 and y>51:
        q4+=1

print(q1*q2*q3*q4)
