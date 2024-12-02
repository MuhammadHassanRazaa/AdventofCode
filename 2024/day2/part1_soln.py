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

total_safe = sum(1 for report in data if is_safe(report))

print("Total Safe Reports:", total_safe)
