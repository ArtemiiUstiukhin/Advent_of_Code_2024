input = open("./day_9/input.txt", "r").read()

numbers = [(int(n), False) for n in input[0::2]]
gaps = [(int(n), []) for n in input[1::2]]

for i in range(len(numbers)):
    number, _ = numbers[-(i+1)]
    for j in range(len(gaps) - i):
        gap, shifted_numbers = gaps[j]
        gap_free_space = gap - sum(length for _, length in shifted_numbers)
        if gap_free_space >= number:
            gaps[j][1].append((len(numbers)-(i+1), number))
            numbers[-(i+1)] = (number, True)
            break

position = 0
checksum = 0

def sum_consecutive_integers(m, n):
    return n * (2 * m + n - 1) // 2

for i in range(len(gaps)):
    number, is_shifted = numbers[i]
    if not is_shifted:
        checksum += sum_consecutive_integers(position, number) * i
    position += number

    gap, shifted_numbers = gaps[i]
    positions_shift = 0
    for file_id, length in shifted_numbers:
        checksum += sum_consecutive_integers(position + positions_shift, length) * file_id
        positions_shift += length
    position += gap

last_number, is_shifted = numbers[-1]
if not is_shifted:
    checksum += sum_consecutive_integers(position, last_number) * (len(numbers) - 1)
    position += last_number

print(checksum)