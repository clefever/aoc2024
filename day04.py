import adventofcode


def part1(input: list[str]) -> int:
    """
    >>> part1(["MMMSXXMASM", "MSAMXMSMSA", "AMXSXMAAMM", "MSAMASMSMX", "XMASAMXAMM",\
               "XXAMMXXAMA", "SMSMSASXSS", "SAXAMASAAA", "MAMMMXMMMM", "MXMXAXMASX"])
    18
    """
    sum = 0
    grid = [list(line) for line in input]
    max_y = len(grid)
    max_x = len(grid[0])
    for y in range(max_y):
        for x in range(max_x):
            if grid[y][x] != 'X':
                continue
            if x < max_x - 3 and grid[y][x+1] == 'M' and grid[y][x+2] == 'A' and grid[y][x+3] == 'S':
                sum += 1
            if x > 2 and grid[y][x-1] == 'M' and grid[y][x-2] == 'A' and grid[y][x-3] == 'S':
                sum += 1
            if y < max_y - 3 and grid[y+1][x] == 'M' and grid[y+2][x] == 'A' and grid[y+3][x] == 'S':
                sum += 1
            if y > 2 and grid[y-1][x] == 'M' and grid[y-2][x] == 'A' and grid[y-3][x] == 'S':
                sum += 1
            if x < max_x - 3 and y < max_y - 3 and grid[y+1][x+1] == 'M' and grid[y+2][x+2] == 'A' and grid[y+3][x+3] == 'S':
                sum += 1
            if x > 2 and y < max_y - 3 and grid[y+1][x-1] == 'M' and grid[y+2][x-2] == 'A' and grid[y+3][x-3] == 'S':
                sum += 1
            if x < max_x - 3 and y > 2 and grid[y-1][x+1] == 'M' and grid[y-2][x+2] == 'A' and grid[y-3][x+3] == 'S':
                sum += 1
            if x > 2 and y > 2 and grid[y-1][x-1] == 'M' and grid[y-2][x-2] == 'A' and grid[y-3][x-3] == 'S':
                sum += 1
    return sum


def part2(input: list[str]) -> int:
    """
    >>> part2(["MMMSXXMASM", "MSAMXMSMSA", "AMXSXMAAMM", "MSAMASMSMX", "XMASAMXAMM",\
               "XXAMMXXAMA", "SMSMSASXSS", "SAXAMASAAA", "MAMMMXMMMM", "MXMXAXMASX"])
    9
    """
    sum = 0
    grid = [list(line) for line in input]
    max_y = len(grid)
    max_x = len(grid[0])
    for y in range(max_y-2):
        for x in range(max_x-2):
            if grid[y][x] != 'M' and grid[y][x] != 'S' and grid[y+1][x+1] != 'A':
                continue
            if grid[y][x] == 'M' and grid[y][x+2] == 'M' and grid[y+1][x+1] == 'A' and grid[y+2][x] == 'S' and grid[y+2][x+2] == 'S':
                sum += 1
            elif grid[y][x] == 'S' and grid[y][x+2] == 'M' and grid[y+1][x+1] == 'A' and grid[y+2][x] == 'S' and grid[y+2][x+2] == 'M':
                sum += 1
            elif grid[y][x] == 'S' and grid[y][x+2] == 'S' and grid[y+1][x+1] == 'A' and grid[y+2][x] == 'M' and grid[y+2][x+2] == 'M':
                sum += 1
            elif grid[y][x] == 'M' and grid[y][x+2] == 'S' and grid[y+1][x+1] == 'A' and grid[y+2][x] == 'M' and grid[y+2][x+2] == 'S':
                sum += 1
    return sum


def main():
    puzzle_input = adventofcode.read_input(4)
    adventofcode.answer(1, 2603, part1(puzzle_input))
    adventofcode.answer(2, 1965, part2(puzzle_input))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
