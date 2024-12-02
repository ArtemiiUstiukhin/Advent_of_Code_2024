safe_count = 0

with open("day_2/test_input.txt", "r") as file:
    for line in file:
        levels = list(map(int, line.strip().split()))
        
        if not levels:
            continue
        
        is_increasing = all(
            levels[i] < levels[i+1] and 1 <= levels[i+1] - levels[i] <= 3
            for i in range(len(levels) - 1)
        )
        
        is_decreasing = all(
            levels[i] > levels[i+1] and 1 <= levels[i] - levels[i+1] <= 3
            for i in range(len(levels) - 1)
        )
        
        if is_increasing or is_decreasing:
            safe_count += 1

print(f"Number of safe reports: {safe_count}")
