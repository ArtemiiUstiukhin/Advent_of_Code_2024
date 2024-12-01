input = open("./day_1/input.txt", "r").read()

left_list = [int(line.split()[0]) for line in input.split("\n")]
right_list = [int(line.split()[1]) for line in input.split("\n")]

left_list.sort()
right_list.sort()

total_distance = sum(abs(left_number - right_number) for left_number, right_number in zip(left_list, right_list))
print(total_distance)