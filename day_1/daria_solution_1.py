
# Parse into two lists
list_1 = []
list_2 = []

# Open and read the file
with open("day_1/test_input.txt") as file:
    for line in file:
        i_1, i_2 = line.strip().split('   ')
        list_1.append(int(i_1))
        list_2.append(int(i_2))


# Sort
list_1.sort()
list_2.sort()

# Calculate differences
differences = [abs(a - b) for a, b in zip(list_1, list_2)]

# Sum up
total_distance = sum(differences)

print(f"The total distance between the lists is: {total_distance}")