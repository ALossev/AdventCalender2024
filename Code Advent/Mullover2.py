import re

with open('mul.txt', 'r') as file:
    memory = file.read()
instruction_pattern = r"do\(\)|don't\(\)|mul\(\d+,\d+\)"
instructions = re.findall(instruction_pattern, memory)

enabled = True
result_sum = 0
for instruction in instructions:
    if instruction == "do()":
        enabled = True
    elif instruction == "don't()":
        enabled = False
    elif instruction.startswith("mul(") and enabled:
        # Extract numbers and calculate product
        nums = re.findall(r"\d+", instruction)
        product = int(nums[0]) * int(nums[1])
        result_sum += product

print("Sum of all results of enabled mul instructions is:", result_sum)