from collections import defaultdict
import heapq

# Read the disk map from the file
with open(r'C:\Users\omega\OneDrive\Desktop\IT 388\2024_09.txt') as f:
    disk_map = f.read().strip()
    print("Disk map content:", disk_map)  # Print to verify the content

# Step 1: Parse the disk map to create a list of lengths
lengths = [int(num) for num in disk_map]

# Step 2: Initialize dictionaries to keep track of filled file segments and gaps
filled_grid = {}  # ID: [start, length]
gaps = defaultdict(list)  # length: [start]

# Step 3: Populate the filled_grid and gaps from the lengths list
cur_pos = 0
for i, num in enumerate(lengths):
    if i % 2 == 0:  # Even indices are file segments
        filled_grid[i // 2] = [cur_pos, num]
    else:  # Odd indices are gaps
        if num > 0:
            heapq.heappush(gaps[num], cur_pos)
    cur_pos += num

# Step 4: Move files to compact the disk
for i in sorted(filled_grid.keys(), reverse=True):
    file_start_pos, file_len = filled_grid[i]
    # Find the best possible gap that can fit the file
    possible_gaps = sorted([[gaps[gap_len][0], gap_len] for gap_len in gaps if gap_len >= file_len])
    if possible_gaps:
        gap_start_pos, gap_len = possible_gaps[0]
        if file_start_pos > gap_start_pos:
            # Move the file to the gap
            filled_grid[i] = [gap_start_pos, file_len]
            remaining_gap_len = gap_len - file_len
            heapq.heappop(gaps[gap_len])  # Remove the used gap
            if not gaps[gap_len]:
                del gaps[gap_len]  # Clean up empty gaps
            if remaining_gap_len:
                heapq.heappush(gaps[remaining_gap_len], gap_start_pos + file_len)

# Step 5: Calculate the checksum
# The checksum is the sum of (position * file ID) for each file block
checksum = sum(num * (start * length + (length * (length - 1)) // 2)
               for num, (start, length) in filled_grid.items())  # (start) + (start + 1) + ... + (start + length - 1)

print("The resulting checksum is:", checksum)
