import adventofcode


def part1(input: list[str]) -> int:
    """
    >>> part1(["....#.....", ".........#", "..........", "..#.......", ".......#..",\
               "..........", ".#..^.....", "........#.", "#.........", "......#..."])
    41
    """
    grid = {}
    loc = (-1, -1)
    dir = (0, -1)
    for y in range(len(input)):
        for x in range(len(input[0])):
            grid[(x,y)] = input[y][x]
            if input[y][x] == "^":
                loc = (x, y)
    visited = {loc}
    while True:
        next_loc = (loc[0] + dir[0], loc[1] + dir[1])
        if next_loc not in grid:
            break
        if grid[next_loc] == "#":
            dir = next_dir(dir)
            next_loc = (loc[0] + dir[0], loc[1] + dir[1])
        loc = next_loc
        visited.add(loc)
    return len(visited)


def part2(input: str) -> int:
    """
    >>> part2(["....#.....", ".........#", "..........", "..#.......", ".......#..",\
               "..........", ".#..^.....", "........#.", "#.........", "......#..."])
    6
    """
    loops = 0
    grid = {}
    start_loc = (-1, -1)
    for y in range(len(input)):
        for x in range(len(input[0])):
            grid[(x,y)] = input[y][x]
            if input[y][x] == "^":
                start_loc = (x, y)
    for y in range(len(input)):
        for x in range(len(input[0])):
            if grid[(x,y)] != ".":
                continue
            dir = (0, -1)
            loc = start_loc
            visited = {(loc, dir)}
            copy = grid.copy()
            copy[(x,y)] = "#"
            while True:
                next_loc = (loc[0] + dir[0], loc[1] + dir[1])
                if next_loc not in copy:
                    break
                while copy[next_loc] == "#":
                    dir = next_dir(dir)
                    next_loc = (loc[0] + dir[0], loc[1] + dir[1])
                loc = next_loc
                if (loc, dir) in visited:
                    loops += 1
                    break
                visited.add((loc, dir))
    return loops


def next_dir(dir):
    if dir == (0, 1):
        return (-1, 0)
    if dir == (1, 0):
        return (0, 1)
    if dir == (0, -1):
        return (1, 0)
    if dir == (-1, 0):
        return (0, -1)


def main():
    puzzle_input = adventofcode.read_input(6)
    adventofcode.answer(1, 4711, part1(puzzle_input))
    adventofcode.answer(2, 1562, part2(puzzle_input))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
