from heapq import heappop, heappush

# Function to read the maze from a file
def read_maze_from_file(filename):
    with open(filename, 'r') as file:
        puzzle_input = file.read().strip()
    return puzzle_input

def part2(puzzle_input):
    grid = puzzle_input.split('\n')
    m, n = len(grid), len(grid[0])
    
    # Find the start (S) and end (E) positions
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'E':
                end = (i, j)

    # Remove 'E' from the grid and replace it with '.' since we're focusing on paths
    grid[end[0]] = grid[end[0]].replace('E', '.')
    
    # Helper function to check if a tile can be visited
    def can_visit(d, i, j, score):
        prev_score = visited.get((d, i, j))
        if prev_score and prev_score < score:
            return False
        visited[(d, i, j)] = score
        return True

    # Directions: East (0), South (1), West (2), North (3)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Priority queue for the Dijkstra-like approach
    heap = [(0, 0, *start, {start})]  # (score, direction, i, j, path)
    visited = {}  # Keeps track of visited states: (direction, i, j) -> score
    lowest_score = None  # Tracks the lowest score to reach the end
    winning_paths = set()  # Tracks all tiles that are part of the best paths

    # Main loop for Dijkstra-like search
    while heap:
        score, d, i, j, path = heappop(heap)
        
        # If we have already found a lower score than the current path, stop exploring
        if lowest_score and lowest_score < score:
            break

        # If we reach the end, update the best path set
        if (i, j) == end:
            lowest_score = score
            winning_paths |= path  # Add current path to the set of winning paths
            continue

        # Skip if this state has been visited with a better score
        if not can_visit(d, i, j, score):
            continue

        # Move forward in the current direction
        x = i + directions[d][0]
        y = j + directions[d][1]
        if grid[x][y] == '.' and can_visit(d, x, y, score + 1):
            heappush(heap, (score + 1, d, x, y, path | {(x, y)}))
        
        # Rotate left (counter-clockwise) by 90 degrees
        left = (d - 1) % 4
        if can_visit(left, i, j, score + 1000):
            heappush(heap, (score + 1000, left, i, j, path))

        # Rotate right (clockwise) by 90 degrees
        right = (d + 1) % 4
        if can_visit(right, i, j, score + 1000):
            heappush(heap, (score + 1000, right, i, j, path))

    return len(winning_paths)

# Read the maze from the file (replace 'maze.txt' with the actual file path)
filename = 'day16'
puzzle_input = read_maze_from_file(filename)

# Call the function to calculate the number of tiles that are part of the best path
print(part2(puzzle_input))  # Output will be the number of tiles on the best paths
