def count_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    mas_patterns = ["MAS", "SAM"]
    
    # Iterate through all possible center points for the X-MAS pattern
    for r in range(1, rows - 1):  # Avoid edges for top/bottom
        for c in range(1, cols - 1):  # Avoid edges for left/right
            # Check for X-MAS
            for top_left in mas_patterns:
                for bottom_right in mas_patterns:
                    if (
                        # Top-left diagonal "MAS" or "SAM"
                        grid[r - 1][c - 1] == top_left[0] and
                        grid[r][c] == top_left[1] and
                        grid[r + 1][c + 1] == top_left[2] and
                        # Bottom-right diagonal "MAS" or "SAM"
                        grid[r + 1][c - 1] == bottom_right[0] and
                        grid[r][c] == bottom_right[1] and
                        grid[r - 1][c + 1] == bottom_right[2]
                    ):
                        count += 1
    return count

# Read the file and prepare the grid
with open('xmas.txt', 'r') as file:
    grid = file.read().strip().split('\n')  # Split into rows and remove trailing spaces

# Convert grid into a 2D list (list of lists)
grid = [list(row) for row in grid]

# Count occurrences of "XMAS" and "SMAX"
result = count_xmas(grid)
print(f"Total occurrences of 'XMAS' : {result}")