def read_input(filename):
    with open(filename, "r") as file:
        content = file.read()

    ordering_rules_section, updates_section = content.strip().split("\n\n")

    ordering_rules = []
    for line in ordering_rules_section.strip().split("\n"):
        if line.strip():
            x, y = line.strip().split("|")
            ordering_rules.append((int(x), int(y)))

    updates = []
    for line in updates_section.strip().split("\n"):
        if line.strip():
            update = [int(num) for num in line.strip().split(",")]
            updates.append(update)

    return ordering_rules, updates


def is_update_correct(ordering_rules, update):
    position_map = {page: idx for idx, page in enumerate(update)}

    for x, y in ordering_rules:
        if x in position_map and y in position_map:
            # x must come before y
            if position_map[x] >= position_map[y]:
                return False  # Rule violated
    return True


def get_middle_page(update):
    n = len(update)
    middle_index = (n - 1) // 2
    return update[middle_index]


def main():
    ordering_rules, updates = read_input("day_5/test_input.txt")

    total_middle_pages_sum = 0
    correctly_ordered_updates = []
    for update in updates:
        if is_update_correct(ordering_rules, update):
            correctly_ordered_updates.append(update)
            middle_page = get_middle_page(update)
            total_middle_pages_sum += middle_page

    print(f"Total sum of middle page numbers: {total_middle_pages_sum}")


main()
