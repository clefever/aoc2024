import adventofcode


def part1(input: list[str]) -> int:
    """
    >>> part1(["89010123", "78121874", "87430965", "96549874", "45678903", "32019012", "01329801", "10456732"])
    36
    """
    max_x = len(input[0])
    max_y = len(input)
    grid = {(x,y): int(input[y][x]) for y in range(max_y) for x in range(max_x)}
    trailheads = [key for key in grid if grid[key] == 0]
    return sum(len(set(score_trail(grid, max_x, max_y, pos))) for pos in trailheads)


def part2(input: list[str]) -> int:
    """
    >>> part2(["89010123", "78121874", "87430965", "96549874", "45678903", "32019012", "01329801", "10456732"])
    81
    """
    max_x = len(input[0])
    max_y = len(input)
    grid = {(x,y): int(input[y][x]) for y in range(max_y) for x in range(max_x)}
    trailheads = [key for key in grid if grid[key] == 0]
    return sum(len(score_trail(grid, max_x, max_y, pos)) for pos in trailheads)


def score_trail(grid: dict[tuple[int, int], int], max_x: int, max_y: int, pos: tuple[int, int]) -> list[tuple[int, int]]:
    if pos[0] < 0 or pos[0] >= max_x or pos[1] < 0 or pos[1] >= max_y:
        return []
    if grid[pos] == 9:
        return [pos]
    positions = []
    if (pos[0]+1, pos[1]) in grid and grid[(pos[0]+1, pos[1])] == grid[pos] + 1:
        positions.extend(score_trail(grid, max_x, max_y, (pos[0]+1, pos[1])))
    if (pos[0]-1, pos[1]) in grid and grid[(pos[0]-1, pos[1])] == grid[pos] + 1:
        positions.extend(score_trail(grid, max_x, max_y, (pos[0]-1, pos[1])))
    if (pos[0], pos[1]+1) in grid and grid[(pos[0], pos[1]+1)] == grid[pos] + 1:
        positions.extend(score_trail(grid, max_x, max_y, (pos[0], pos[1]+1)))
    if (pos[0], pos[1]-1) in grid and grid[(pos[0], pos[1]-1)] == grid[pos] + 1:
        positions.extend(score_trail(grid, max_x, max_y, (pos[0], pos[1]-1)))
    return positions


def main():
    puzzle_input = adventofcode.read_input(10)
    adventofcode.answer(1, 482, part1(puzzle_input))
    adventofcode.answer(2, 1094, part2(puzzle_input))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
