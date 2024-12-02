# Define the file path
file_path = "input.txt"

# Initialize empty lists
list1 = []
list2 = []

# Read data from the file
with open(file_path, "r") as file:
    for line in file:
        # Split the line into two numbers
        numbers = line.split()
        if len(numbers) == 2:  # Ensure the line has exactly two numbers
            list1.append(int(numbers[0]))
            list2.append(int(numbers[1]))

# Sort both lists
sorted_list1 = sorted(list1)
sorted_list2 = sorted(list2)

# Calculate the total distance
total_distance = sum(abs(a - b) for a, b in zip(sorted_list1, sorted_list2))

# Print the results
print("Total Distance:", total_distance)
