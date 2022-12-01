def parse_input(filename):
    with open(filename) as f:
        return [line.strip() for line in f]

def create_elves(input):
    elves = [0]

    for line in input:
        if line == '':
            elves.append(0)
        else:
            elves[-1] += int(line)

    return elves

def part_one(elves):
    return max(elves)

def part_two(elves):
    return sum(sorted(elves)[-3:])

if __name__ == '__main__':
    input = parse_input('input.txt')
    elves = create_elves(input)
    print(part_one(elves))
    print(part_two(elves))