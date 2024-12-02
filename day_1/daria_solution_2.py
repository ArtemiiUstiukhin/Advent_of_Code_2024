from collections import Counter

# Parse into two lists
list_1 = []

ctn = Counter()

# Open and read the file
with open("day_1/test_input.txt") as file:
    for line in file:
        i_1, i_2 = line.strip().split('   ')
        list_1.append(int(i_1))
        ctn[int(i_2)] += 1

# Find unique values in list_1 and count occurrences in list_2
unique_list_1 = set(list_1)

# Calculate similarity score
similarity_score = sum(i * ctn[i] for i in unique_list_1)

print(f"The similarity score is: {similarity_score}")