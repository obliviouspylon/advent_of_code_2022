

def part1(fileName):
    score = 0
    X = 1
    cycles = 0
    with open(fileName,"r") as f:
        line = f.readline()
        while line:
            # Code goes here
            line = line.replace("\n","")
            if line == "noop":
                cycle = 1
                action = ["",""]
            else:
                action = line.split(" ")
                cycle = 2
            for i in range(cycle):
                cycles = cycles + 1
                if cycles%40 == 20:
                    score = score + cycles*X
                    print(str(cycles) + ": " + str(X))
            if action[0] == "addx":
                print(str(cycles) + ": " + str(action[1]))
                X = X + int(action[1])
                print(X)
            line = f.readline()
    return score

def part2(fileName):
    score = 0
    X = 1
    cycles = 0
    # crtDefault = ["#"]
    # for i in range(38):
    #     crtDefault.append(".")
    # crtDefault.append("#")
    with open(fileName,"r") as f:
        # crtRow = crtDefault.copy()
        line = f.readline()
        crtRow=[]
        while line:
            # Code goes here
            line = line.replace("\n","")
            if line == "noop":
                cycle = 1
                action = ["",""]
            else:
                action = line.split(" ")
                cycle = 2
            for i in range(cycle):
                value = abs(cycles%40 - X)
                if value == 1 or value == 0:
                    # crtRow[X-1] = "#"
                    crtRow.append("#")
                else:
                    # crtRow[X-1] = "."
                    crtRow.append(".")
                cycles = cycles + 1
                if cycles%40 == 0:
                    # score = score + cycles*X
                    # print(str(cycles) + ": " + str(X))
                    for i in crtRow:
                        print(i,end="")
                    print("\n",end="")
                    # crtRow = crtDefault.copy()
                    crtRow = []
            if action[0] == "addx":
                # print(str(cycles) + ": " + str(action[1]))
                X = X + int(action[1])
            line = f.readline()
    return score


if __name__ == "__main__":
    day = 10
    # print(part1("Day " + str(day) + "\\example.txt"))
    # print(part1("Day " + str(day) + "\\input.txt"))
    # print(part2("Day " + str(day) + "\\example.txt"))
    print(part2("Day " + str(day) + "\\input.txt"))