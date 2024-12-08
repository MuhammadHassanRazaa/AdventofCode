import re

file_path = "input.txt"

pattern = r"mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)"

with open(file_path, 'r') as file:
    content = file.read()

matches = re.findall(pattern, content)
    
total_sum = sum(int(x) * int(y) for x, y in matches)

print("Total Sum:", total_sum)
