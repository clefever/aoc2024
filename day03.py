import adventofcode
import re


def part1(input: str) -> int:
    """
    >>> part1("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))")
    161
    """
    sum = 0
    x = re.findall(r"mul\((\d+),(\d+)\)", input)
    for tup in x:
        sum += int(tup[0]) * int(tup[1])
    return sum


def part2(input: str) -> int:
    """
    >>> part2("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))")
    48
    """
    enableds = []
    disableds = []
    muls = []
    sum = 0
    for match in re.finditer(r"do\(\)", input):
        enableds.append(match.start())
    for match in re.finditer(r"don't\(\)", input):
        disableds.append(match.start())
    for match in re.finditer(r"mul\((\d+),(\d+)\)", input):
        muls.append((match.start(), match.groups()))
    the_max = range(0, max(enableds[-1], disableds[-1], muls[-1][0])+1)
    enabled = True
    for x in the_max:
        if x in enableds:
            enabled = True
        if x in disableds:
            enabled = False
        if x in [tup[0] for tup in muls] and enabled:
            for i, val in enumerate(muls):
                if val[0] == x:
                    sum += int(muls[i][1][0]) * int(muls[i][1][1])
                    break
    return sum


def main():
    puzzle_input = adventofcode.read_input(3)
    input_line = "".join(puzzle_input)
    adventofcode.answer(1, 173731097, part1(input_line))
    adventofcode.answer(2, 93729253, part2(input_line))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
