def count_xmas(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    count = 0
    
    directions = [
        (0, 1),   # right
        (0, -1),  # left
        (1, 0),   # down
        (-1, 0),  # up
        (1, 1),   # diagonal down-right
        (1, -1),  # diagonal down-left
        (-1, 1),  # diagonal up-right
        (-1, -1), # diagonal up-left
    ]
    
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def find_word(x, y, dx, dy):
        for k in range(word_len):
            nx, ny = x + k * dx, y + k * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[k]:
                return False
        return True

    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if find_word(i, j, dx, dy):
                    count += 1

    return count

def read_grid_from_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

filename = 'input.txt'
word = "XMAS"

result = count_xmas(read_grid_from_file(filename), word)
print(f"The word '{word}' appears {result} times in the grid.")
