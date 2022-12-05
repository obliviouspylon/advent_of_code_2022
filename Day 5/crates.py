import itertools

def part1(fileName):
    with open(fileName,"r") as f:
        line = f.readline()
        num_stacks = int(len(line)/4)
        instructions = False
        stacks = []
        for i in range(num_stacks):
            stacks.append([])
        while line:
            # Code goes here
            if line == "\n" and instructions == False:
                instructions = True
                for i in range(num_stacks):
                    stacks[i-1].pop(0)
            
            if instructions:
                if line == "\n":
                    line = f.readline()
                    continue

                moves = line.replace("move ","").replace(" from ",";").replace(" to ",";").replace("\n","").split(";")
                for move in range(int(moves[0])):
                    stacks[int(moves[2])-1].append(stacks[int(moves[1])-1][-1])
                    stacks[int(moves[1])-1].pop()
            else:
                for i in range(num_stacks):
                    if line[(i-1)*4+1] != " ":
                        stacks[i-1].insert(0,line[(i-1)*4+1])

            line = f.readline()
    top_crates = ""
    for i in range(num_stacks):
        top_crates = top_crates + str(stacks[i][-1])
    return top_crates

def part2(fileName):
    with open(fileName,"r") as f:
        line = f.readline()
        num_stacks = int(len(line)/4)
        instructions = False
        stacks = []
        for i in range(num_stacks):
            stacks.append([])
        while line:
            # Code goes here
            if line == "\n" and instructions == False:
                instructions = True
                for i in range(num_stacks):
                    stacks[i-1].pop(0)
            
            if instructions:
                if line == "\n":
                    line = f.readline()
                    continue

                moves = line.replace("move ","").replace(" from ",";").replace(" to ",";").replace("\n","").split(";")
                for crate in stacks[int(moves[1])-1][-int(moves[0]):]:
                    stacks[int(moves[2])-1].append(crate)
                for move in range(int(moves[0])):
                    stacks[int(moves[1])-1].pop()
            else:
                for i in range(num_stacks):
                    if line[(i-1)*4+1] != " ":
                        stacks[i-1].insert(0,line[(i-1)*4+1])

            line = f.readline()
    top_crates = ""
    for i in range(num_stacks):
        top_crates = top_crates + str(stacks[i][-1])
    return top_crates


if __name__ == "__main__":
    day = 5
    # print(part1("Day " + str(day) + "\\input.txt"))
    # print(part1("Day " + str(day) + "\\example.txt"))
    print(part2("Day " + str(day) + "\\input.txt"))
    print(part2("Day " + str(day) + "\\example.txt"))