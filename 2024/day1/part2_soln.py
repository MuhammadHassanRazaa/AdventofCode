from collections import Counter

file_path = "input.txt"

list1 = []
list2 = []

with open(file_path, "r") as file:
    for line in file:
        numbers = line.split()
        if len(numbers) == 2:
            list1.append(int(numbers[0]))
            list2.append(int(numbers[1]))

right_counts = Counter(list2)

similarity_score = sum(num * right_counts[num] for num in list1)

print("Total Similarity Score:", similarity_score)
