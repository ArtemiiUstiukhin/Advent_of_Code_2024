with open('day_9/test_input.txt', 'r') as f:
    disk_map = f.read().strip()

file_lengths = []
free_lengths = []

for idx, char in enumerate(disk_map):
    length = int(char)
    if idx % 2 == 0:
        file_lengths.append(length)
    else:
        free_lengths.append(length)

disk_representation = []
file_id = 0

for i in range(len(file_lengths)):
    for _ in range(file_lengths[i]):
        disk_representation.append(str(file_id))

    if i < len(free_lengths):
        for _ in range(free_lengths[i]):
            disk_representation.append('.')
    file_id += 1

if len(free_lengths) > len(file_lengths):
    for _ in range(free_lengths[-1]):
        disk_representation.append('.')


file_positions = {}
current_index = 0

for fid in range(file_id):
    length = file_lengths[fid]
    if length == 0:
        continue
    start = current_index
    end = current_index + length - 1
    file_positions[fid] = (start, end)
    current_index += length
    if fid < len(free_lengths):
        current_index += free_lengths[fid]

sorted_files = sorted(file_positions.keys(), reverse=True)

def find_leftmost_free_space(disk, file_length):
    consecutive = 0
    start_pos = 0
    for idx, block in enumerate(disk):
        if block == '.':
            if consecutive == 0:
                start_pos = idx
            consecutive += 1
            if consecutive == file_length:
                return start_pos
        else:
            consecutive = 0
    return None

for fid in sorted_files:
    start, end = file_positions[fid]
    length = end - start + 1
    target_start = find_leftmost_free_space(disk_representation, length)

    if target_start is not None and target_start < start:
        for i in range(length):
            disk_representation[target_start + i] = str(fid)
            disk_representation[start + i] = '.'
        file_positions[fid] = (target_start, target_start + length - 1)


checksum = 0
for position, block in enumerate(disk_representation):
    if block != '.':
        fid = int(block)
        checksum += position * fid

print(f"Filesystem Checksum: {checksum}")
