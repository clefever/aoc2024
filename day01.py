import adventofcode


def part1(input: list[list[int]]) -> int:
    """
    >>> part1([[3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3]])
    11
    """
    input[0].sort()
    input[1].sort()
    return sum(abs(input[0][i] - input[1][i]) for i in range(len(input[0])))


def part2(input: list[list[int]]) -> int:
    """
    >>> part2([[3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3]])
    31
    """
    return sum(input[0][i] * input[1].count(input[0][i]) for i in range(len(input[0])))


def main():
    puzzle_input = adventofcode.read_input(1)
    input_nums = list(map(list, zip(*[[int(num) for num in line.split()] for line in puzzle_input])))
    adventofcode.answer(1, 2580760, part1(input_nums))
    adventofcode.answer(2, 25358365, part2(input_nums))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
