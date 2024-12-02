import adventofcode


def part1(input):
    """
    >>> part1([[7, 6, 4, 2, 1], [1, 2, 7, 8, 9], [9, 7, 6, 2, 1],\
               [1, 3, 2, 4, 5], [8, 6, 4, 4, 1], [1, 3, 6, 7, 9]])
    2
    """
    sum = 0
    for nums in input:
        is_good = True
        positives = 0
        negatives = 0
        zeros = 0
        for i in range(len(nums)-1):
            if abs(nums[i+1] - nums[i]) > 3:
                is_good = False

            if nums[i+1] > nums[i]:
                positives += 1
            elif nums[i+1] < nums[i]:
                negatives += 1
            else:
                zeros += 1
        if is_good and (positives == 0 or negatives == 0) and zeros == 0:
            sum += 1
    return sum


def part2(input):
    """
    >>> part2([[7, 6, 4, 2, 1], [1, 2, 7, 8, 9], [9, 7, 6, 2, 1],\
               [1, 3, 2, 4, 5], [8, 6, 4, 4, 1], [1, 3, 6, 7, 9]])
    4
    """
    sum = 0
    for nums in input:
        solved = False
        for y in range(len(nums)):
            copy = nums.copy()
            copy.pop(y)
            is_good = True
            positives = 0
            negatives = 0
            zeros = 0

            for i in range(len(nums)-1):
                if abs(nums[i+1] - nums[i]) > 3:
                    is_good = False

                if nums[i+1] > nums[i]:
                    positives += 1
                elif nums[i+1] < nums[i]:
                    negatives += 1
                else:
                    zeros += 1
            if is_good and (positives == 0 or negatives == 0) and zeros == 0:
                sum += 1
                solved = True
                break

        if solved == False: 
            for y in range(len(nums)):
                copy = nums.copy()
                copy.pop(y)
                is_good = True
                positives = 0
                negatives = 0
                zeros = 0

                for i in range(len(copy)-1):
                    if abs(copy[i+1] - copy[i]) > 3:
                        is_good = False

                    if copy[i+1] > copy[i]:
                        positives += 1
                    elif copy[i+1] < copy[i]:
                        negatives += 1
                    else:
                        zeros += 1
                if is_good and (positives == 0 or negatives == 0) and zeros == 0:
                    sum += 1
                    break

    return sum


def main():
    puzzle_input = adventofcode.read_input(2)
    input_nums = [[int(num) for num in line.split()] for line in puzzle_input]
    adventofcode.answer(1, 564, part1(input_nums))
    adventofcode.answer(2, 604, part2(input_nums))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
