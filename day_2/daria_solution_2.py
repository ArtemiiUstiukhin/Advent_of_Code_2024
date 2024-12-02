safe_count = 0

def is_safe(levels):
    if len(levels) <= 1:
        return True

    is_increasing = all(
        levels[i] < levels[i+1] and 1 <= levels[i+1] - levels[i] <= 3
        for i in range(len(levels) - 1)
    )
    is_decreasing = all(
        levels[i] > levels[i+1] and 1 <= levels[i] - levels[i+1] <= 3
        for i in range(len(levels) - 1)
    )
    return is_increasing or is_decreasing

with open("day_2/test_input.txt", "r") as file:
    for line in file:
        levels = list(map(int, line.strip().split()))
        
        if is_safe(levels):
            safe_count += 1
        else:
            for bad_level in range(len(levels)):
                line_without_bad_level = levels[:bad_level] + levels[bad_level+1:]
                if is_safe(line_without_bad_level):
                    safe_count += 1
                    break 

print(f"Number of safe reports: {safe_count}")