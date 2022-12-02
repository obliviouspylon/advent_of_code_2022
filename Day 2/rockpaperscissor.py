


def part1(fileName):
    score = 0
    with open(fileName,"r") as f:
        line = f.readline()
        while line:
            # Let 1 be Rock, 2 be paper, 3 for scissor
            action = line.replace("\n","").replace("A","1").replace("X","1").replace("B","2").replace("Y","2").replace("C","3").replace("Z","3")
            action = action.split(" ")
            score = score + int(action[1])

            if action[1] == action[0]:
                score = score + 3
            elif action[1] == "1" and action[0] == "3":
                score = score + 6
            elif action[1] == "2" and action[0] == "1":
                score = score + 6
            elif action[1] == "3" and action[0] == "2":
                score = score + 6
            line = f.readline()
    return score

choice = {
    "A" : {
        "0": 3,
        "3" : 1,
        "6" : 2
    },
    "B" : {
        "0": 1,
        "3" : 2,
        "6" : 3
    },
    "C" : {
        "0": 2,
        "3" : 3,
        "6" : 1
    },
}
def part2(fileName):
    score = 0
    with open(fileName,"r") as f:
        line = f.readline()
        while line:
            # Let 1 be Rock, 2 be paper, 3 for scissor
            action = line.replace("\n","").replace("X","0").replace("Y","3").replace("Z","6")
            action = action.split(" ")
            score = score + int(action[1]) + choice[action[0]][action[1]]
            line = f.readline()
    return score

if __name__ == "__main__":
    # print(part1("Day 2\\input.txt"))
    print(part2("Day 2\\input.txt"))
    # print(part1("Day 2\\example.txt"))
    print(part2("Day 2\\example.txt"))