import re

file_path = "input.txt"

mul_pattern = r"mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)"
do_pattern = r"do\(\s*\)"
dont_pattern = r"don't\(\s*\)"

with open(file_path, 'r') as file:
        content = file.read()

tokens = re.split(r"(?=mul\(|do\(|don't\()", content)

mul_enabled = True
total_sum = 0

for token in tokens:
    if re.match(do_pattern, token):  # Enable multiplication
        mul_enabled = True
    elif re.match(dont_pattern, token):  # Disable multiplication
        mul_enabled = False
    elif mul_enabled:  # Only process mul() if enabled
        match = re.match(mul_pattern, token)
        if match:
            x, y = map(int, match.groups())
            total_sum += x * y

print("Total Sum:", total_sum)
