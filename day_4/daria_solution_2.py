def read_grid(filename):
    with open(filename, 'r') as f:
        grid = [list(line.strip()) for line in f if line.strip()]
    return grid

def count_xmas_patterns(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if grid[i][j] == 'A':
                # D1: (i-1, j-1), (i, j), (i+1, j+1)
                diag1 = [grid[i-1][j-1], grid[i][j], grid[i+1][j+1]]
                # D2: (i-1, j+1), (i, j), (i+1, j-1)
                diag2 = [grid[i-1][j+1], grid[i][j], grid[i+1][j-1]]

                sequences = ['MAS', 'SAM']

                diag1_str = ''.join(diag1)
                diag2_str = ''.join(diag2)

                if (diag1_str in sequences) and (diag2_str in sequences):
                    count += 1
    return count

grid = read_grid('day_4/test_input.txt')
total_count = count_xmas_patterns(grid)
print(f"Total occurrences of 'X-MAS': {total_count}")
