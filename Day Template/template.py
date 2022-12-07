

def part1(fileName):
    score = 0
    with open(fileName,"r") as f:
        line = f.readline()
        while line:
            # Code goes here

            

            line = f.readline()
    return score




if __name__ == "__main__":
    day = 0
    print(part1("Day " + str(day) + "\\example.txt"))
    # print(part1("Day " + str(day) + "\\input.txt"))
    # print(part2("Day " + str(day) + "\\example.txt"))
    # print(part2("Day " + str(day) + "\\input.txt"))