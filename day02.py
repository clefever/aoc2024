import adventofcode


def part1(input: list[list[int]]) -> int:
    """
    >>> part1([[7, 6, 4, 2, 1], [1, 2, 7, 8, 9], [9, 7, 6, 2, 1],\
               [1, 3, 2, 4, 5], [8, 6, 4, 4, 1], [1, 3, 6, 7, 9]])
    2
    """
    return sum(is_safe(nums) for nums in input)


def part2(input: list[list[int]]) -> int:
    """
    >>> part2([[7, 6, 4, 2, 1], [1, 2, 7, 8, 9], [9, 7, 6, 2, 1],\
               [1, 3, 2, 4, 5], [8, 6, 4, 4, 1], [1, 3, 6, 7, 9]])
    4
    """
    return sum(any(is_safe_tolerant(nums, i) for i in range(len(nums))) for nums in input)


def is_safe(list: list[int]) -> bool:
    return (all(abs(list[i] - list[i-1]) <= 3 for i in range(1, len(list))) and
           (all(list[i] > list[i-1] for i in range(1, len(list))) or
           all(list[i] < list[i-1] for i in range(1, len(list)))))


def is_safe_tolerant(list: list[int], i: int) -> bool:
    copy = list.copy()
    copy.pop(i)
    return is_safe(copy)


def main():
    puzzle_input = adventofcode.read_input(2)
    input_nums = [[int(num) for num in line.split()] for line in puzzle_input]
    adventofcode.answer(1, 564, part1(input_nums))
    adventofcode.answer(2, 604, part2(input_nums))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
