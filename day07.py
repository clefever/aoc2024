import adventofcode
from itertools import product


def part1(input: list[str]) -> int:
    """
    >>> part1(["190: 10 19", "3267: 81 40 27", "83: 17 5", "156: 15 6", "7290: 6 8 6 15",\
               "161011: 16 10 13", "192: 17 8 14", "21037: 9 7 18 13", "292: 11 6 16 20"])
    3749
    """
    sum = 0
    for line in input:
        split = line.split(":")
        val = int(split[0])
        nums = [int(num) for num in split[1].split(" ") if num != ""]
        op_flags = pow(2, len(nums)-1)
        for op in range(op_flags):
            s = nums[0]
            for i in range(0, len(nums)-1):
                if op & (1 << i) == 1 << i:
                    s += nums[i+1]
                else:
                    s *= nums[i+1]
            if s == val:
                sum += val
                break
    return sum


def part2(input: list[str]) -> int:
    """
    >>> part2(["190: 10 19", "3267: 81 40 27", "83: 17 5", "156: 15 6", "7290: 6 8 6 15",\
               "161011: 16 10 13", "192: 17 8 14", "21037: 9 7 18 13", "292: 11 6 16 20"])
    11387
    """
    sum = 0
    for line in input:
        split = line.split(":")
        val = int(split[0])
        nums = [int(num) for num in split[1].split(" ") if num != ""]
        for combo in product(["*", "+", "||"], repeat=len(nums)-1):
            s = nums[0]
            for i in range(len(combo)):
                if combo[i] == "+":
                    s += nums[i+1]
                if combo[i] == "*":
                    s *= nums[i+1]
                if combo[i] == "||":
                    s = int(str(s)+str(nums[i+1]))
            if s == val:
                sum += val
                break
    return sum


def main():
    puzzle_input = adventofcode.read_input(7)
    adventofcode.answer(1, 5540634308362, part1(puzzle_input))
    adventofcode.answer(2, 472290821152397, part2(puzzle_input))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
