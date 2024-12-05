import adventofcode
from math import floor
from functools import cmp_to_key


def part1(rules: list[list[int]], updates: list[list[int]]) -> int:
    """
    >>> part1([[47, 53], [97, 13], [97, 61], [97, 47], [75, 29], [61, 13], [75, 53],\
               [29, 13], [97, 29], [53, 29], [61, 53], [97, 53], [61, 29], [47, 13],\
               [75, 47], [97, 75], [47, 61], [75, 61], [47, 29], [75, 13], [53, 13]],\
               [[75,47,61,53,29], [97,61,53,29,13], [75,29,13], [75,97,47,61,53],\
               [61,13,29], [97,13,75,29,47]])
    143
    """
    sum = 0
    for update in updates:
        satifies = True
        for page in update:
            if not satisfies_rules(page, rules, update):
                satifies = False
                break
        if satifies:
            sum += update[floor(len(update)/2)]
    return sum


def part2(rules: list[list[int]], updates: list[list[int]]) -> int:
    """
    >>> part2([[47, 53], [97, 13], [97, 61], [97, 47], [75, 29], [61, 13], [75, 53],\
               [29, 13], [97, 29], [53, 29], [61, 53], [97, 53], [61, 29], [47, 13],\
               [75, 47], [97, 75], [47, 61], [75, 61], [47, 29], [75, 13], [53, 13]],\
               [[75,47,61,53,29], [97,61,53,29,13], [75,29,13], [75,97,47,61,53],\
               [61,13,29], [97,13,75,29,47]])
    123
    """
    sum = 0
    bad_updates = []
    for update in updates:
        for page in update:
            if not satisfies_rules(page, rules, update):
                bad_updates.append(update)
                break
    for update in bad_updates:
        update = sorted(update, key=cmp_to_key(lambda item1, item2: compare(item1, item2, rules)))
        sum += update[floor(len(update)/2)]
    return sum


def satisfies_rules(page: int, rules: list[list[int]], update: list[int]) -> bool:
    for rule in rules:
        if rule[0] not in update or rule[1] not in update:
            continue
        if rule[0] == page:
            if update.index(page) > update.index(rule[1]):
                return False
        elif rule[1] == page:
            if update.index(page) < update.index(rule[0]):
                return False
    return True


def compare(page1, page2, rules):
    for rule in rules:
        if rule[0] == page1 and rule[1] == page2:
            return -1
        if rule[0] == page2 and rule[1] == page1:
            return 1
    return 0


def parse_data(input: str) -> tuple[list[list[int]], list[list[int]]]:
    rules = [list(map(int, nums)) for nums in [line.split("|") for line in input if "|" in line]]
    updates = [list(map(int, nums)) for nums in [line.split(",") for line in input if "," in line]]
    return rules, updates


def main():
    puzzle_input = adventofcode.read_input(5)
    data = parse_data(puzzle_input)
    adventofcode.answer(1, 4689, part1(data[0], data[1]))
    adventofcode.answer(2, 6336, part2(data[0], data[1]))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
