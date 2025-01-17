def parse_input(input_data):
    # Separate rules and updates
    rules_section, updates_section = input_data.strip().split("\n\n")
    rules = [tuple(map(int, rule.split("|"))) for rule in rules_section.splitlines()]
    updates = [list(map(int, update.split(","))) for update in updates_section.splitlines()]
    return rules, updates

def is_update_valid(update, rules):
    # Validate if the update adheres to the ordering rules
    update_set = set(update)
    for x, y in rules:
        if x in update_set and y in update_set:
            if update.index(x) > update.index(y):
                return False
    return True

def find_middle_page(update):
    # Find the middle page number of an update
    mid_index = len(update) // 2
    return update[mid_index]

def calculate_sum_of_middle_pages(input_data):
    rules, updates = parse_input(input_data)
    valid_middle_pages = []
    
    for update in updates:
        if is_update_valid(update, rules):
            valid_middle_pages.append(find_middle_page(update))
    
    return sum(valid_middle_pages)

# Example Input
input_data = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

# Calculate and print the result
result = calculate_sum_of_middle_pages(input_data)
print(result)
