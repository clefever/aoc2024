import adventofcode
from itertools import combinations


def part1(input: list[str]) -> int:
    """
    >>> part1(["............", "........0...", ".....0......", ".......0....", "....0.......", "......A.....",\
               "............", "............", "........A...", ".........A..", "............", "............"])
    14
    """
    x_len, y_len = len(input[0]), len(input)
    antennas = {}
    for y in range(len(input)):
        for x in range(len(input[0])):
            if input[y][x] != '.':
                if input[y][x] in antennas:
                    antennas[input[y][x]].append((x, y))
                else:
                    antennas[input[y][x]] = [(x, y)]
    positions = set()
    for ant_list in antennas.values():
        combs = list(combinations(ant_list, 2))
        for comb in combs:
            delta = (comb[0][0] - comb[1][0], comb[0][1] - comb[1][1])
            positions.add((comb[0][0] + delta[0], comb[0][1] + delta[1]))
            positions.add((comb[1][0] - delta[0], comb[1][1] - delta[1]))
    return len(list(filter(lambda x: x[0] >= 0 and x[0] < x_len and x[1] >= 0 and x[1] < y_len, positions)))


def part2(input: list[str]) -> int:
    """
    >>> part2(["............", "........0...", ".....0......", ".......0....", "....0.......", "......A.....",\
               "............", "............", "........A...", ".........A..", "............", "............"])
    34
    """
    x_len, y_len = len(input[0]), len(input)
    antennas = {}
    for y in range(len(input)):
        for x in range(len(input[0])):
            if input[y][x] != '.':
                if input[y][x] in antennas:
                    antennas[input[y][x]].append((x, y))
                else:
                    antennas[input[y][x]] = [(x, y)]
    positions = set()
    for ant_list in antennas.values():
        combs = list(combinations(ant_list, 2))
        for comb in combs:
            delta = (comb[0][0] - comb[1][0], comb[0][1] - comb[1][1])
            node1 = (comb[0][0], comb[0][1])
            while True:
                node1 = (node1[0] + delta[0], node1[1] + delta[1])
                if node1[0] >= 0 and node1[0] < x_len and node1[1] >= 0 and node1[1] < y_len:
                    positions.add(node1)
                else:
                    break
            node2 = (comb[0][0], comb[0][1])
            while True:
                node2 = (node2[0] - delta[0], node2[1] - delta[1])
                if node2[0] >= 0 and node2[0] < x_len and node2[1] >= 0 and node2[1] < y_len:
                    positions.add(node2)
                else:
                    break
            positions.add((comb[0][0], comb[0][1]))
            positions.add((comb[1][0], comb[1][1]))
    return len(positions)


def main():
    puzzle_input = adventofcode.read_input(8)
    adventofcode.answer(1, 313, part1(puzzle_input))
    adventofcode.answer(2, 1064, part2(puzzle_input))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
