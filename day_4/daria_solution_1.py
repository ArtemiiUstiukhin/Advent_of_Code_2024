import re

def count_word_in_lines(word, lines):
    pattern = '(?=' + word + ')'
    total = 0
    for line in lines:
        matches = re.findall(pattern, line)
        total += len(matches)
    return total

def get_diagonals(grid, direction):
    rows = len(grid)
    cols = len(grid[0])
    diagonals = []
    
    if direction == 'TL-BR':  # top-left to bottom-right
        # Diagonals starting from the first row
        for col in range(cols):
            i, j = 0, col
            diag = ''
            while i < rows and j < cols:
                diag += grid[i][j]
                i += 1
                j += 1
            diagonals.append(diag)
        # Diagonals starting from the first column (excluding [0,0])
        for row in range(1, rows):
            i, j = row, 0
            diag = ''
            while i < rows and j < cols:
                diag += grid[i][j]
                i += 1
                j += 1
            diagonals.append(diag)
    elif direction == 'TR-BL':  # Top-right to bottom-left
        # Diagonals starting from the first row
        for col in range(cols-1, -1, -1):
            i, j = 0, col
            diag = ''
            while i < rows and j >= 0:
                diag += grid[i][j]
                i += 1
                j -= 1
            diagonals.append(diag)
        # Diagonals starting from the first column (excluding [0,cols-1])
        for row in range(1, rows):
            i, j = row, cols - 1
            diag = ''
            while i < rows and j >= 0:
                diag += grid[i][j]
                i += 1
                j -= 1
            diagonals.append(diag)
    return diagonals

def read_grid(filename):
    with open(filename, 'r') as f:
        grid = [line.strip() for line in f if line.strip()]
    return grid

def count_all_occurrences(grid, word):
    total = 0
    # ->
    total += count_word_in_lines(word, grid)
    # <-
    reverse_grid = [line[::-1] for line in grid]
    total += count_word_in_lines(word, reverse_grid)
    # Vertical T-B
    cols = [''.join(row[col] for row in grid) for col in range(len(grid[0]))]
    total += count_word_in_lines(word, cols)
    # Vertical B-T
    reverse_cols = [col[::-1] for col in cols]
    total += count_word_in_lines(word, reverse_cols)
    # Diagonal TL - BR
    diagonals_tl_br = get_diagonals(grid, 'TL-BR')
    total += count_word_in_lines(word, diagonals_tl_br)
    # Diagonal BR-TL
    diagonals_tl_br_rev = [diag[::-1] for diag in diagonals_tl_br]
    total += count_word_in_lines(word, diagonals_tl_br_rev)
    # Diagonal TR-BL
    diagonals_tr_bl = get_diagonals(grid, 'TR-BL')
    total += count_word_in_lines(word, diagonals_tr_bl)
    # Diagonal BL-TR
    diagonals_tr_bl_rev = [diag[::-1] for diag in diagonals_tr_bl]
    total += count_word_in_lines(word, diagonals_tr_bl_rev)
    return total


grid = read_grid('day_4/test_input.txt')
word = 'XMAS'
total_count = count_all_occurrences(grid, word)
print(f"Total occurrences of '{word}': {total_count}")
