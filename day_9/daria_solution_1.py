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


while True:
    try:
        first_free = disk_representation.index('.')
    except ValueError:
        break
    
    last_file = -1
    for i in range(len(disk_representation)-1, first_free, -1):
        if disk_representation[i] != '.':
            last_file = i
            break
    
    if last_file == -1:
        break
    
    disk_representation[first_free] = disk_representation[last_file]
    disk_representation[last_file] = '.'
    

checksum = 0
for position, block in enumerate(disk_representation):
    if block != '.':
        file_id = int(block)
        checksum += position * file_id


print(f"Filesystem Checksum: {checksum}")
