import adventofcode


def part1(input):
    """
    >>> part1([[3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3]])
    11
    """
    input[0].sort()
    input[1].sort()

    sum = 0
    for i in range(len(input[0])):
        sum += abs(input[0][i] - input[1][i])

    return sum


def part2(input):
    """
    >>> part2([[3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3]])
    31
    """
    sum = 0
    for i in range(len(input[0])):
        similarity = input[1].count(input[0][i])
        sum += input[0][i] * similarity

    return sum


def main():
    puzzle_input = adventofcode.read_input(1)
    input_nums = [list(l) for l in zip(*[[int(n) for n in num.split()] for num in puzzle_input])]
    adventofcode.answer(1, 2580760, part1(input_nums))
    adventofcode.answer(2, 25358365, part2(input_nums))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
