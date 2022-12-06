

def part1(fileName):
    with open(fileName,"r") as f:
        found = False
        line = f.readline()
        while line:
            # Code goes here
            for i in range(len(line)-4):
                string = line[i:i+4]
                same = False
                for j in string:
                    change = string.replace(j,"")
                    if len(change) < 3:
                        same = True
                        break
                if same == False:
                    print(str(i+4))
                    break
                
            line = f.readline()
    return ""

def part2(fileName):
    charcters = 14
    with open(fileName,"r") as f:
        found = False
        line = f.readline()
        while line:
            # Code goes here
            for i in range(len(line)-charcters):
                string = line[i:i+charcters]
                same = False
                for j in string:
                    change = string.replace(j,"")
                    if len(change) < charcters-1:
                        same = True
                        break
                if same == False:
                    print(str(i+charcters))
                    break
                
            line = f.readline()
    return ""


if __name__ == "__main__":
    day = 6
    # print(part1("Day " + str(day) + "\\input.txt"))
    # print(part1("Day " + str(day) + "\\example.txt"))
    print(part2("Day " + str(day) + "\\input.txt"))
    # print(part2("Day " + str(day) + "\\example.txt"))