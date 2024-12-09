import adventofcode


def part1(input: str) -> int:
    """
    >>> part1("2333133121414131402")
    1928
    """
    blocks = [i//2 if i % 2 == 0 else -1 for i in range(len(input)) for _ in range(int(input[i]))]
    end = len(blocks) - 1
    for i in range(len(blocks)):
        if i >= end:
            break
        if blocks[i] == -1:
            blocks[i], blocks[end] = blocks[end], blocks[i]
            while blocks[end] == -1:
                end -= 1
    return sum(i * blocks[i] for i in range(len(blocks)) if blocks[i] != -1)


def part2(input: str) -> int:
    """
    >>> part2("2333133121414131402")
    2858
    """
    blocks = [i//2 if i % 2 == 0 else -1 for i in range(len(input)) for _ in range(int(input[i]))]
    end = len(blocks) - 1
    moved_indexes = []
    while True:
        end_index, end_length = calc_end_filesystem(blocks, end, moved_indexes)
        free_index = get_span_of_size(blocks, end_length, end_index)
        if free_index != -1:
            moved_indexes.append(free_index)
            for j in range(end_length):
                blocks[free_index+j], blocks[end_index+j] = blocks[end_index+j], blocks[free_index+j]
        end = end_index - 1
        if end < 0:
            break
    return sum(i * blocks[i] for i in range(len(blocks)) if blocks[i] != -1)


def get_span_of_size(filesystem: list[int], size: int, max_index: int) -> int:
    sum = 0
    index = -1
    for i in range(max_index):
        if filesystem[i] == -1:
            if index == -1:
                index = i
            sum += 1
            if sum >= size:
                break
        else:
            sum = 0
            index = -1
    if sum >= size:
        return index
    else:
        return -1


def calc_space(filesystem: list[int], index: int) -> int:
    sum = 0
    while True:
        if filesystem[index] == -1:
            sum += 1
            index += 1
        else:
            break
    return sum


# Returns filesystem (index, length)
def calc_end_filesystem(filesystem: list[int], end: int, moved_indexes: list[int]) -> tuple[int, int]:
    while filesystem[end] == -1:
        end -= 1
    num = filesystem[end]
    sum = 0
    while True:
        if filesystem[end] == num:
            sum += 1
            end -= 1
        else:
            if end + 1 in moved_indexes:
                while filesystem[end] == -1:
                    end -= 1
                num = filesystem[end]
                sum = 0
            else:
                break
    return end + 1, sum


def main():
    puzzle_input = adventofcode.read_input(9)
    adventofcode.answer(1, 6401092019345, part1(puzzle_input))
    adventofcode.answer(2, 6431472344710, part2(puzzle_input))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
