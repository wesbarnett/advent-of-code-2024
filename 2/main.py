from argparse import ArgumentParser
from aoc_tool import get_input, submit

YEAR, DAY = 2024, 2


def parse_input(aoc_input):
    return [[int(x) for x in line.split()] for line in aoc_input.splitlines()]


def part1(aoc_input, do_submit=False):
    res = sum(
        [
            all([0 < abs(data[i + 1] - data[i]) < 4 for i in range(len(data) - 1)])
            and (
                all([(data[i + 1] - data[i]) < 0 for i in range(len(data) - 1)])
                or all([(data[i + 1] - data[i]) > 0 for i in range(len(data) - 1)])
            )
            for data in parse_input(aoc_input)
        ]
    )

    if do_submit:
        submit(res, YEAR, DAY, 1)

    return res


def part2(aoc_input, do_submit=False):
    res = None

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
#   print(part2(aoc_input, args.submit_part2))
