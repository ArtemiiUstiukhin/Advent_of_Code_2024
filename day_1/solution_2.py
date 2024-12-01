import numpy as np

input = open("./day_1/input.txt", "r").read()

left_list = [int(line.split()[0]) for line in input.split("\n")]
right_list = [int(line.split()[1]) for line in input.split("\n")]

left_list_numners_unique, left_list_numbers_occur = np.unique(left_list, return_counts=True)
left_list_map = dict(zip(list(left_list_numners_unique), list(left_list_numbers_occur)))

right_list_numners_unique, right_list_numbers_occur = np.unique(right_list, return_counts=True)
right_list_map = dict(zip(list(right_list_numners_unique), list(right_list_numbers_occur)))

similarity_score = sum(occur * number * right_list_map.get(number, 0) for number, occur in left_list_map.items())
print(similarity_score)