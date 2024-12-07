from functools import cmp_to_key

input = open("./day_5/input.txt", "r").read()

rules, updates = [section.split('\n') for section in input.split('\n\n')]
rules_map = set([tuple(rule.split("|")) for rule in rules])

def compare_pages(p1, p2):
    return 1 if (p1, p2) in rules_map else -1 if (p2, p1) in rules_map else 0

middle_page_number_sum = 0
for update in updates:
    update_array = update.split(",")
    original_update = update_array.copy()
    sorted_update = sorted(update_array, key=cmp_to_key(compare_pages), reverse=True)
    if original_update != sorted_update:
        middle_page_number_sum += int(sorted_update[len(sorted_update)//2])

print(middle_page_number_sum)