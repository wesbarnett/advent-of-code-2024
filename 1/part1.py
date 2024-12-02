from aoc_tool import get_input, submit

YEAR, DAY, LEVEL = 2024, 1, 1

if __name__ == "__main__":

    aoc_input = get_input(YEAR, DAY)
    list1, list2 = [], []

    for line in aoc_input.splitlines():
        x1, x2 = line.split()
        list1.append(int(x1))
        list2.append(int(x2))

    list1.sort()
    list2.sort()

    res = sum([abs(x1 - x2) for x1, x2 in zip(list1, list2)])
    print(res)

    submit(res, YEAR, DAY, LEVEL)
