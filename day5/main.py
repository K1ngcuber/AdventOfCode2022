def read_input(path):
    crates = []
    instructions = []

    with open(path) as f:
        for line in f:
            if("[" not in line):
                break
            for (i, index) in zip(range(1, len(line), 4), range(len(line)//4)):
                if line[i] != " ":

                    crates.append((index, line[i]))

        for line in f:
            if line != "\n":
                instructions.append(line.strip().split(" "))

    crates.reverse()

    return crates, instructions


def part1(crates, instructions):
    result = ""
    stacks = {}

    for (index, crate) in crates:
        if index+1 in stacks.keys():
            stacks[index+1].append(crate)
        else:
            stacks[index+1] = [crate]

    for instruction in instructions:
        amount = int(instruction[1])
        from_index = int(instruction[3])
        to_index = int(instruction[5])

        for _ in range(amount):
            crate = stacks[from_index].pop()
            stacks[to_index].append(crate)

    for key in stacks.keys():
        result += stacks[key].pop()

    return result[::-1]


def part2(crates, instructions):
    result = ""
    stacks = {}

    for (index, crate) in crates:
        if index+1 in stacks.keys():
            stacks[index+1].append(crate)
        else:
            stacks[index+1] = [crate]

    for instruction in instructions:
        amount = int(instruction[1])
        from_index = int(instruction[3])
        to_index = int(instruction[5])

        moved_crates = []

        for _ in range(amount):
            moved_crates.append(stacks[from_index].pop())

        moved_crates.reverse()
        for crate in moved_crates:

            stacks[to_index].append(crate)

    for key in stacks.keys():
        result += stacks[key].pop()

    return result[::-1]


if __name__ == "__main__":
    (crates, instructions) = read_input("input.txt")

    print("Part 1: {}".format(part1(crates, instructions)))
    print("Part 2: {}".format(part2(crates, instructions)))
