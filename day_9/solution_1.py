input = open("./day_9/input.txt", "r").read()

numbers = [int(n) for n in input[0::2]]
gaps = [int(n) for n in input[1::2]]

def sum_consecutive_integers(m, n):
    return n * (2 * m + n - 1) // 2

position = 0
checksum = 0
left_file_id = 0
right_file_id = len(numbers) - 1

while len(numbers) > 0 and len(gaps) > 0:
    leftmost_number = numbers.pop(0)
    checksum += sum_consecutive_integers(position, leftmost_number) * left_file_id
    position += leftmost_number
    left_file_id += 1
    if len(numbers) == 0:
        break
    gap = gaps.pop(0)
    while gap > 0 and len(numbers) > 0:
        rightmost_number = numbers.pop(-1)
        diff = min(gap, rightmost_number)
        checksum += sum_consecutive_integers(position, diff) * right_file_id
        position += diff
        right_file_id -= 1
        if rightmost_number > gap:
            numbers.append(rightmost_number - diff)
            right_file_id += 1
        
        gap -= rightmost_number

print(checksum)
