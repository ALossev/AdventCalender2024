from collections import deque
def parse_map(map_lines):
    return [list(map(int, line.strip())) for line in map_lines]

def find_neighbors(grid, r, c):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    rows, cols = len(grid), len(grid[0])
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            yield nr, nc

def bfs_trailhead(grid, start):
    queue = deque([start])
    visited = set([start])
    reachable_nines = set()
    while queue:
        r, c = queue.popleft()
        for nr, nc in find_neighbors(grid, r, c):
            if (nr, nc) not in visited and grid[nr][nc] == grid[r][c] + 1:
                visited.add((nr, nc))
                queue.append((nr, nc))
                if grid[nr][nc] == 9:
                    reachable_nines.add((nr, nc))
    return len(reachable_nines)

def dfs_trailhead(grid, r, c, visited, memo):
    if (r, c) in memo:
        return memo[(r, c)]
    
    total_paths = 0
    for nr, nc in find_neighbors(grid, r, c):
        if (nr, nc) not in visited and grid[nr][nc] == grid[r][c] + 1:
            visited.add((nr, nc))
            if grid[nr][nc] == 9:
                total_paths += 1  # Reached height 9
            else:
                total_paths += dfs_trailhead(grid, nr, nc, visited, memo)
            visited.remove((nr, nc))
    
    memo[(r, c)] = total_paths
    return total_paths

def calculate_scores_and_ratings(grid):
    trailheads = [(r, c) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == 0]
    total_score = 0
    total_rating = 0
    
    for r, c in trailheads:
        total_score += bfs_trailhead(grid, (r, c))
        total_rating += dfs_trailhead(grid, r, c, set([(r, c)]), {})
    
    return total_score, total_rating
with open('day10.txt', 'r') as file:
    grid = parse_map(file.readlines())

total_score, total_rating = calculate_scores_and_ratings(grid)
print("Total score of all trailheads:", total_score)
print("Total rating of all trailheads:", total_rating)
