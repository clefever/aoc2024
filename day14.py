import adventofcode
import re


def part1(input: list[str], width: int, height: int) -> int:
    """
    >>> part1(["p=0,4 v=3,-3", "p=6,3 v=-1,-3", "p=10,3 v=-1,2", "p=2,0 v=2,-1", "p=0,0 v=1,3", "p=3,0 v=-2,-2",\
               "p=7,6 v=-1,-3", "p=3,0 v=-1,-2", "p=9,3 v=2,3", "p=7,3 v=-1,2", "p=2,4 v=2,-3", "p=9,5 v=-3,-3"], 11, 7)
    12
    """



    robots = []
    for line in input:
        x = re.match(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", line)
        robots.append(Robot(int(x.group(1)), int(x.group(2)), int(x.group(3)), int(x.group(4))))

    for _ in range(100):
        for robot in robots:
            robot.x = (robot.x + robot.vx) % width
            robot.y = (robot.y + robot.vy) % height

    quadrants = [0, 0, 0, 0]
    for robot in robots:
        if robot.x < width // 2:
            if robot.y < height // 2:
                quadrants[0] += 1
            elif robot.y > height // 2:
                quadrants[1] += 1
        elif robot.x > width // 2:
            if robot.y < height // 2:
                quadrants[2] += 1
            elif robot.y > height // 2:
                quadrants[3] += 1    
    product = 1
    for val in quadrants:
        product *= val

    return product


def part2(input: list[str], width: int, height: int) -> int:
    robots = []
    for line in input:
        x = re.match(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", line)
        robots.append(Robot(int(x.group(1)), int(x.group(2)), int(x.group(3)), int(x.group(4))))

    i = 0
    while True:
        i += 1
        for robot in robots:
            robot.x = (robot.x + robot.vx) % width
            robot.y = (robot.y + robot.vy) % height
        if (i - 46) % 101 == 0:
            print(i)
            print('------------')
            for y in range(height):
                for x in range(width):
                    found = False
                    for robot in robots:
                        if robot.x == x and robot.y == y:
                            print('R', end='')
                            found = True
                            break
                    if not found:
                        print('.', end='')
                print()
            print('------------')


class Robot:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def __repr__(self):
        return f'p={self.x},{self.y} v={self.vx},{self.vy}'


def main():
    puzzle_input = adventofcode.read_input(14)
    adventofcode.answer(1, 222062148, part1(puzzle_input, 101, 103))
    #adventofcode.answer(2, 7520, part2(puzzle_input, 101, 103))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
