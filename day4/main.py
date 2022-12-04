def parse_input(filename):
    with open(filename,'r') as f:
        return f.read()

def part1(data):
    result = 0

    for line in data.splitlines():
        (first,second) = line.split(",")

        (firstStart,firstEnd) = first.split("-")
        (secondStart,secondEnd) = second.split("-")


        if (int(firstStart) <= int(secondStart) and int(secondEnd) <= int(firstEnd)): 
            result += 1

        elif(int(secondStart) <= int(firstStart) and int(firstEnd) <= int(secondEnd)):
            result += 1

    return result

def part2(data):
    result = 0

    for line in data.splitlines():
        (first,second) = line.split(",")
        (firstStart,firstEnd) = first.split("-")
        (secondStart,secondEnd) = second.split("-")

        #second start is contained in first range
        if int(secondStart) >= int(firstStart) and int(secondStart) <= int(firstEnd):
            result += 1
        
        #second end is contained in first range
        elif int(secondEnd) >= int(firstStart) and int(secondEnd) <= int(firstEnd):
            result += 1

        #first start is contained in second range
        elif int(firstStart) >= int(secondStart) and int(firstStart) <= int(secondEnd):
            result += 1
        
        #first end is contained in second range
        elif int(firstEnd) >= int(secondStart) and int(firstEnd) <= int(secondEnd):
            result += 1
        
    return result

        

if __name__ == '__main__':
    input = parse_input('input.txt')
    print("Part 1: {}".format(part1(input)))
    print("Part 2: {}".format(part2(input)))