from argparse import ArgumentParser
from collections import Counter
from aoc_tool import get_input, submit

YEAR, DAY = 2024, 1


def parse_input(aoc_input):
    list1, list2 = [], []

    for line in aoc_input.splitlines():
        x1, x2 = line.split()
        list1.append(int(x1))
        list2.append(int(x2))
    return list1, list2


def part1(aoc_input, do_submit=False):
    list1, list2 = parse_input(aoc_input)

    list1.sort()
    list2.sort()

    res = sum([abs(x1 - x2) for x1, x2 in zip(list1, list2)])

    if do_submit:
        submit(res, YEAR, DAY, 1)

    return res


def part2(aoc_input, do_submit=False):
    list1, list2 = parse_input(aoc_input)

    counts2 = Counter(list2)

    res = sum(x1 * counts2[x1] for x1, x2 in zip(list1, list2))

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
