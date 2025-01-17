from collections import defaultdict, deque

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

def reorder_update(update, rules):
    # Build a directed graph from the rules
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    update_set = set(update)
    
    for x, y in rules:
        if x in update_set and y in update_set:
            graph[x].append(y)
            in_degree[y] += 1
            if x not in in_degree:
                in_degree[x] = 0
    
    # Perform Topological Sort
    queue = deque([node for node in update if in_degree[node] == 0])
    sorted_update = []
    
    while queue:
        node = queue.popleft()
        sorted_update.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_update

def find_middle_page(update):
    # Find the middle page number of an update
    mid_index = len(update) // 2
    return update[mid_index]

def calculate_sum_of_reordered_middle_pages(input_data):
    rules, updates = parse_input(input_data)
    reordered_middle_pages = []
    
    for update in updates:
        if not is_update_valid(update, rules):
            reordered_update = reorder_update(update, rules)
            reordered_middle_pages.append(find_middle_page(reordered_update))
    
    return sum(reordered_middle_pages)

with open('5input.txt', 'r') as file:
    input_data = file.read()

result = calculate_sum_of_reordered_middle_pages(input_data)
print(result)