

def part1(fileName):
    big = 0
    holder = 0
    with open(fileName,"r") as f:
        line = f.readline()
        while line:
            if line == "\n":
                if holder >= big:
                    big = holder
                holder = 0
            else:
                holder = holder + int(line.replace("\n",""))
            line = f.readline()
    return big

def part2(fileName):
    big = [-1,-2,-3]
    holder = 0
    with open(fileName,"r") as f:
        line = f.readline()
        while line:
            if line == "\n":
                if holder >= min(big):
                    for i in range(len(big)):
                        if big[i] == min(big):
                            big[i] = holder
                            break
                holder = 0
            else:
                holder = holder + int(line.replace("\n",""))
            line = f.readline()
    return sum(big)

if __name__ == "__main__":
    print(part1("Day 1\\input.txt"))
    print(part2("Day 1\\input.txt"))
    # print(main("Day 1\\example.txt"))