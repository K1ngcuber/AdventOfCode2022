ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def read_file(path):
    with open(path, 'r') as input_file:
        return input_file.read()


def part1(data):
    result = 0

    for line in data.splitlines():
        # split string into two parts
        part_one = line[:int(len(line)/2)]
        part_two = line[int(len(line)/2):]

        for letter in ALPHABET:
            if letter in part_one and letter in part_two:
                result += ALPHABET.index(letter) + 1
                break

    return result


def part2(data):
    result = 0

    rucksacks = []

    for line in data.splitlines():
        rucksacks.append(line)

    for i in range(0, len(rucksacks), 3):
        for letter in ALPHABET:
            if letter in rucksacks[i] and letter in rucksacks[i+1] and letter in rucksacks[i+2]:
                result += ALPHABET.index(letter) + 1
                break

    return result


if __name__ == '__main__':
    input_data = read_file('input.txt')
    print("Part1 {}".format(part1(input_data)))
    print("Part2 {}".format(part2(input_data)))
