def parse_input(filename):
    with open(filename) as f:
        return [line.strip() for line in f]

def part1(input):
    result = 0

    for game in input:
        score = 0
        (player_one,player_two) = game.split(" ")
        # a = ROCK, b = PAPER, c = SCISSORS
        # x = ROCK, y = PAPER, z = SCISSORS
        player_two = player_two.replace("X","A").replace("Y","B").replace("Z","C")

        result += ord(player_two) - 64
        score += ord(player_two) - 64

        if player_one == player_two:
            result += 3
            score += 3

        elif player_one == "A" and player_two == "B" or player_one == "B" and player_two == "C" or player_one == "C" and player_two == "A":
            result += 6
            score += 6
        


    return result

def part2(input):
    result = 0

    for game in input:

        (player_one,expected_result) = game.split(" ")

        win = ""
        loose = ""
        draw = ""
        if(player_one == "A"):
            win = "B"
            loose = "C"
            draw = "A"
        elif(player_one == "B"):
            win = "C"
            loose = "A"
            draw = "B"
        elif(player_one == "C"):
            win = "A"
            loose = "B"
            draw = "C"

        if(expected_result == "X"):
            #loose
            result += ord(loose) - 64
        elif(expected_result == "Y"):
            #draw
            result += ord(draw) - 64
            result += 3
        elif(expected_result == "Z"):
            #win
            result += ord(win) - 64
            result += 6

    return result


if __name__ == '__main__':
    input = parse_input('input.txt')
    print("Part 1 {}".format(part1(input)))
    print("Part 2 {}".format(part2(input)))