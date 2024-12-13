machines = []
with open("test_input.txt", "r") as f:
    lines = [line.strip() for line in f if line.strip()]
    for i in range(0, len(lines), 3):
        A = lines[i]
        B = lines[i + 1]
        lineP = lines[i + 2]

        instructionsA = A.split(":")[1].strip()

        xa_str, ya_str = instructionsA.split(",")
        xa = int(xa_str.split("+")[1])
        ya = int(ya_str.split("+")[1])

        partB = B.split(":")[1].strip()
        xb_str, yb_str = partB.split(",")
        xb = int(xb_str.split("+")[1])
        yb = int(yb_str.split("+")[1])

        partP = lineP.split(":")[1].strip()
        xp_str, yp_str = partP.split(",")
        xp = int(xp_str.split("=")[1])
        yp = int(yp_str.split("=")[1])

        machines.append((xa, ya, xb, yb, xp, yp))

max_prizes = 0
total_cost = 0

for xa, ya, xb, yb, xp, yp in machines:
    min_cost = None
    for A in range(101):
        for B in range(101):
            X = A * xa + B * xb
            Y = A * ya + B * yb
            if X == xp and Y == yp:
                cost = 3 * A + B
                if min_cost is None or cost < min_cost:
                    min_cost = cost
    if min_cost is not None:
        max_prizes += 1
        total_cost += min_cost

print(f"Maximum prizes: {max_prizes}")
print(f"Total cost: {total_cost}")
