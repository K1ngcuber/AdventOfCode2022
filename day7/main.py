class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __str__(self):
        return str(self.name)

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, File):
            return self.name == __o.name


class Node:
    def __init__(self, name):
        self.children = []
        self.files = []
        self.name = name
        self.parent = None

    def __str__(self):
        return str(self.name) + " " + str(self.sum_files())

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Node):
            return self.name == __o.name

    def sum_files(self):
        total = 0
        for file in self.files:
            total += int(file.size)

        for child in self.children:
            total += child.sum_files()

        return total

    def add_child(self, child):
        self.children.append(child)

    def add_file(self, file):
        self.files.append(file)


def generate_directories(data):
    node = Node("/")
    for line in data.splitlines():
        if line[0] == "$":
            command = line.split(" ")
            if command[1] == "cd" and command[2] == "..":
                node = node.parent
            elif command[1] == "cd" and command[2] == "/":
                while node.parent is not None:
                    node = node.parent
            elif command[1] == "cd" and command[2] not in node.children:
                new_node = Node(command[2])
                new_node.parent = node
                node.add_child(new_node)
                node = new_node
            elif command[1] == "cd" and command[2] in node.children:
                node = node.children[node.children.index(command[2])]

        else:
            (file, size) = line.split(" ")
            if file != "dir":
                node.add_file(File(size, file))

    while node.parent is not None:
        node = node.parent

    return node


def print_tree(tree):
    print(tree)
    for child in tree.children:
        print_tree(child)


def find_by_size(tree, size):
    result = 0
    for child in tree.children:
        if child.sum_files() <= size:
            result += child.sum_files()
        result += find_by_size(child, size)

    return result


def find_delete_candidates(tree, size):
    result = []

    if tree.sum_files() >= size:
        result.append(tree)

    for child in tree.children:
        result += find_delete_candidates(child, size)

    return result


def part1(data):
    directories = generate_directories(data)
    return find_by_size(directories, 100000)


def part2(data):
    directories = generate_directories(data)

    needed_space = 70000000 - directories.sum_files()

    candidates = find_delete_candidates(directories, 30000000 - needed_space)

    minimum = 2147483647
    for candidate in candidates:
        if candidate.sum_files() < minimum:
            minimum = candidate.sum_files()

    return minimum


if __name__ == "__main__":

    with open("input.txt") as f:
        data = f.read()

    # Part 1
    print("Part 1:", part1(data))

    # Part 2
    print("Part 2:", part2(data))
