def is_safe(report):
    differences = [report[i+1] - report[i] for i in range(len(report) - 1)]
    
    # Check if all differences are between 1 and 3 (increasing) or -1 and -3 (decreasing)
    increasing = all(1 <= diff <= 3 for diff in differences)
    decreasing = all(-3 <= diff <= -1 for diff in differences)
    
    return increasing or decreasing

def is_safe_with_dampener(report):
    # Check if the report is already safe
    if is_safe(report):
        return True
    
    # Try removing one level at a time and check if the remaining levels are safe
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            return True
    
    return False

def count_safe_reports_with_dampener(reports):
    return sum(1 for report in reports if is_safe_with_dampener(report))

# Read data from the file
with open('codes.txt', 'r') as file:
    data = file.readlines()

# Parse the data into a list of lists of integers
reports = [list(map(int, line.split())) for line in data if line.strip()]

# Count safe reports
safe_count = count_safe_reports_with_dampener(reports)
print(f"Number of safe reports (with Problem Dampener): {safe_count}")
