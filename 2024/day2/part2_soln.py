file_path = "input.txt"

data = []
with open(file_path, "r") as file:
    for line in file:
        data.append(list(map(int, line.split())))

def is_safe(report):
    is_increasing = all(report[i] < report[i + 1] for i in range(len(report) - 1))
    is_decreasing = all(report[i] > report[i + 1] for i in range(len(report) - 1))

    diff_valid = all(1 <= abs(report[i] - report[i + 1]) <= 3 for i in range(len(report) - 1))

    return (is_increasing or is_decreasing) and diff_valid

def can_be_safe_with_dampener(report):
    for i in range(len(report)):
        # Create a new report with one level removed
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            return True
    return False

total_safe = 0
for report in data:
    if is_safe(report) or can_be_safe_with_dampener(report):
        total_safe += 1

print("Total Safe Reports:", total_safe)
