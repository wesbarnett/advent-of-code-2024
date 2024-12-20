from argparse import ArgumentParser
from itertools import pairwise
from aoc_tool import get_input, submit

YEAR, DAY = 2024, 3

def part1(aoc_input, do_submit=False):
    res = 0
    for x in aoc_input.split("mul("):
        y = x.split(",", maxsplit=1)
        try:
            res += int(y[0]) * int(y[1].split(")")[0])
        except:
            continue

    if do_submit:
        submit(res, YEAR, DAY, 1)

    return res


def part2(aoc_input, do_submit=False):
    next_mul_enabled = True
    res = 0
    for x in aoc_input.split("mul("):
        mul_enabled = next_mul_enabled

        dont_index = x.rfind("don't()")
        do_index = x.rfind("do()")

        if dont_index == -1 and do_index == -1:
            pass
        elif dont_index > do_index:
            next_mul_enabled = False
        else:
            next_mul_enabled = True

        y = x.split(",", maxsplit=1)

        try:
            if mul_enabled:
                res += int(y[0]) * int(y[1].split(")")[0])
            else:
                pass
        except:
            continue

    if do_submit:
        submit(res, YEAR, DAY, 2)

    return res



if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--submit-part1", action="store_true")
    parser.add_argument("--submit-part2", action="store_true")
    args = parser.parse_args()

    aoc_input = get_input(YEAR, DAY)

    print(part1(aoc_input, args.submit_part1))
    print(part2(aoc_input, args.submit_part2))
