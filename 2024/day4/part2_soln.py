def count_xmas(grid, patterns):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols
    
    def find_pattern(x, y, pattern):
        for i in range(3):
            for j in range(3):
                if pattern[i][j] == '.' or (is_valid(x + i, y + j) and grid[x + i][y + j] == pattern[i][j]):
                    continue
                else:
                    return False
        return True

    for i in range(rows - 2):
        for j in range(cols - 2):
            for pattern in patterns:
                if find_pattern(i, j, pattern):
                    count += 1

    return count

def read_grid_from_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

filename = 'input.txt'
patterns = [
    [['M', '.', 'S'], ['.', 'A', '.'], ['M', '.', 'S']], # MAS pattern
    [['S', '.', 'S'], ['.', 'A', '.'], ['M', '.', 'M']], # MAS pattern
    [['M', '.', 'M'], ['.', 'A', '.'], ['S', '.', 'S']], # MAS pattern
    [['S', '.', 'M'], ['.', 'A', '.'], ['S', '.', 'M']]  # MAS pattern
]

result = count_xmas(read_grid_from_file(filename), patterns)
print(f"The word 'X-MAS' appears {result} times in the grid.")


