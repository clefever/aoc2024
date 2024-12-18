import adventofcode


def part1(reg_a: int, reg_b: int, reg_c: int, program: list[int]) -> str:
    """
    >>> part1(729, 0, 0, [0, 1, 5, 4, 3, 0])
    '4,6,3,5,6,3,5,2,1,0'
    """
    return ",".join([str(num) for num in run_program(reg_a, reg_b, reg_c, program)])


def part2(program: list[int]) -> int:
    """
    >>> part2([0, 3, 5, 4, 3, 0])
    117440
    """
    length = 1
    reg_a = 0
    while True:
        output = run_program(reg_a, 0, 0, program)
        if output == program:
            return reg_a
        elif output == program[-length:]:
            length += 1
            reg_a *= 8
        else:
            reg_a += 1


def run_program(reg_a: int, reg_b: int, reg_c: int, program: list[int]) -> list[int]:
    output = []
    pointer = 0
    while pointer < len(program)-1:
        increment = True
        if program[pointer] == 0: # adv
            reg_a = reg_a // pow(2, combo_op(program[pointer+1], reg_a, reg_b, reg_c))
        elif program[pointer] == 1: # bxl
            reg_b = reg_b ^ program[pointer+1]
        elif program[pointer] == 2: # bst
            reg_b = combo_op(program[pointer+1], reg_a, reg_b, reg_c) % 8
        elif program[pointer] == 3: # jnz
            if reg_a != 0:
                pointer = program[pointer+1]
                increment = False
        elif program[pointer] == 4: # bxc
            reg_b ^= reg_c
        elif program[pointer] == 5: # out
            output.append(combo_op(program[pointer+1], reg_a, reg_b, reg_c) % 8)
        elif program[pointer] == 6: # bdv
            reg_b = reg_a // pow(2, combo_op(program[pointer+1], reg_a, reg_b, reg_c))
        elif program[pointer] == 7: # cdv
            reg_c = reg_a // pow(2, combo_op(program[pointer+1], reg_a, reg_b, reg_c))
        if increment:
            pointer += 2
    return output


def combo_op(op: int, reg_a: int, reg_b: int, reg_c: int) -> int:
    if op >= 0 and op <=3:
        return op
    elif op == 4:
        return reg_a
    elif op == 5:
        return reg_b
    elif op == 6:
        return reg_c


def main():
    puzzle_input = adventofcode.read_input(17)
    reg_a = int(puzzle_input[0].split()[2])
    reg_b = int(puzzle_input[1].split()[2])
    reg_c = int(puzzle_input[2].split()[2])
    program = [int(n) for n in puzzle_input[4].split()[1].split(',')]
    adventofcode.answer(1, "7,6,1,5,3,1,4,2,6", part1(reg_a, reg_b, reg_c, program))
    adventofcode.answer(2, 164541017976509, part2(program))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
