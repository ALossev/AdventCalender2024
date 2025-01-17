import re

with open('mul.txt', 'r') as file:
    memory = file.read()

pattern = r"mul\(\d+,\d+\)"
matches = re.findall(pattern,memory)

result_sum = 0
for match in matches:
    nums = re.findall(r"\d+", match)
    product = int(nums[0]) * int(nums[1])
    result_sum += product
print("Sum of all results of valid mul instructions is :", result_sum)