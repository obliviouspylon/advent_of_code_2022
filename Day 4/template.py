

def isbetween(range, value):
    if (int(value) >= int(range[0]) and int(value) <= int(range[1])):
        return True
    else:
        return False

def part1(fileName):
    score = 0
    with open(fileName,"r") as f:
        line = f.readline()
        while line:
            # Code goes here
            split = line.replace("\n","").split(",")
            elf1 = split[0].split("-")
            elf2 = split[1].split("-")
            
            if (isbetween(elf1, elf2[0]) and isbetween(elf1, elf2[1])):
                score = score + 1
            elif (isbetween(elf2, elf1[0]) and isbetween(elf2, elf1[1])):
                score = score + 1
            line = f.readline()

    return score

def part2(fileName):
    score = 0
    with open(fileName,"r") as f:
        line = f.readline()
        while line:
            # Code goes here
            split = line.replace("\n","").split(",")
            elf1 = split[0].split("-")
            elf2 = split[1].split("-")

            elf1 = list(range(int(elf1[0]),int(elf1[1])+1))
            elf2 = list(range(int(elf2[0]),int(elf2[1])+1))

            for i in elf1:
                if i in elf2:
                    score = score + 1
                    break
            line = f.readline()

    return score


if __name__ == "__main__":
    # print(part1("Day 4\\input.txt"))
    # print(part1("Day 4\\example.txt"))
    print(part2("Day 4\\input.txt"))
    print(part2("Day 4\\example.txt"))