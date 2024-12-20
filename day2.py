from argparse import ArgumentParser
from itertools import pairwise
from aoc_tool import get_input, submit

YEAR, DAY = 2024, 2


def parse_input(aoc_input):
    return [[int(x) for x in line.split()] for line in aoc_input.splitlines()]


def part1(aoc_input, do_submit=False):
    res = sum(
        [
            all([0 < abs(y - x) < 4 for x, y in pairwise(data)])
            and (all([(y - x) < 0 for x, y in pairwise(data)]) or all([(y - x) > 0 for x, y in pairwise(data)]))
            for data in parse_input(aoc_input)
        ]
    )

    if do_submit:
        submit(res, YEAR, DAY, 1)

    return res


def part2(aoc_input, do_submit=False):
    tot = 0
    for data in parse_input(aoc_input):
        for j in range(len(data)):
            data_slice = data[:j] + data[j + 1 :]
            all_decreasing = all([(y - x) < 0 for x, y in pairwise(data_slice)])
            all_increasing = all([(y - x) > 0 for x, y in pairwise(data_slice)])
            adjacent_rule = all([0 < abs(y - x) < 4 for x, y in pairwise(data_slice)])

            if adjacent_rule and (all_decreasing or all_increasing):
                tot += 1
                break

    res = tot
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
