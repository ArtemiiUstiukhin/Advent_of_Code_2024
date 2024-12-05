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
            update = [int(page) for page in line.strip().split(",")]
            updates.append(update)

    return ordering_rules, updates


def is_update_correct(ordering_rules, update):
    page_positions = {page: index for index, page in enumerate(update)}

    for x, y in ordering_rules:
        if x in page_positions and y in page_positions:
            if page_positions[x] >= page_positions[y]:
                return False
    return True


def correct_update(ordering_rules, update):
    pages_in_update = set(update)

    applicable_rules = []
    for x, y in ordering_rules:
        if x in pages_in_update and y in pages_in_update:
            applicable_rules.append((x, y))

    sorted_pages = []

    while pages_in_update:
        no_rules_pages = []
        for page in pages_in_update:
            is_ready = True
            for x, y in applicable_rules:
                if y == page:
                    is_ready = False
                    break
            if is_ready:
                no_rules_pages.append(page)

        no_rules_pages.sort(key=lambda x: update.index(x))

        for page in no_rules_pages:
            sorted_pages.append(page)
            pages_in_update.remove(page)

            applicable_rules = [rule for rule in applicable_rules if rule[0] != page]

    return sorted_pages


def get_middle_page(update):
    length = len(update)
    middle_index = (length - 1) // 2
    return update[middle_index]


def main():
    ordering_rules, updates = read_input("day_5/test_input.txt")

    total_middle_pages = 0

    for update in updates:
        if not is_update_correct(ordering_rules, update):
            corrected_update = correct_update(ordering_rules, update)
            middle_page = get_middle_page(corrected_update)
            total_middle_pages += middle_page
        else:
            continue

    print("Total sum of middle page numbers after correction:", total_middle_pages)


if __name__ == "__main__":
    main()
