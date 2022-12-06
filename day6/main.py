def read_input():
    with open("input.txt", "r") as f:
        return f.read().splitlines()


def part1(data):
    for line in data:
        print(line)


if __name__ == "__main__":
    data = read_input()
    print("Part 1: ", part1(data))
    print("Part 2: ", part2(data))
