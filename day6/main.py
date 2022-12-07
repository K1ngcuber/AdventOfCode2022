def read_input():
    with open("input.txt", "r") as f:
        return f.read()


def part1(data):
    for letter in range(len(data)-2):
        if(len(set(data[letter:letter+4])) == 4):
            print(letter+4)
            break


def part2(data):
    for letter in range(len(data)-2):
        if(len(set(data[letter:letter+14])) == 14):
            print(letter+1-4)
            break


if __name__ == "__main__":
    data = read_input()
    print("Part 1: ", part1(data))
    print("Part 2: ", part2(data))
