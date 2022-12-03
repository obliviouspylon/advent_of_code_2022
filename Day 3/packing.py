

def part1(fileName):
    score = 0
    with open(fileName,"r") as f:
        line = f.readline()
        while line:
            # Code goes here
            bag1 = line[:int(len(line)/2)]
            bag2 = line[int(len(line)/2):]

            for i in bag1:
                if i in bag2:
                    ASCII = ord(i)
                    # print(i)
                    if ASCII > 96:
                        score = score + ASCII - 96
                    else:
                        score = score + ASCII - 64 + 26
                    break
                else:
                    continue         

            line = f.readline()
    return score


def part2(fileName):
    score = 0
    with open(fileName,"r") as f:
        bag_count = 0
        bags = []
        lines= f.readlines()
        for line in lines:
            if bag_count < 3:
                bags.append(line)
                bag_count = bag_count + 1

            if bag_count == 3:
                # Code goes here
                bags = sorted(bags, key=len)

                for i in bags[0]:
                    if i in bags[1] and i in bags[2]:
                        ASCII = ord(i)
                        # print(i)
                        if ASCII > 96:
                            score = score + ASCII - 96
                        else:
                            score = score + ASCII - 64 + 26
                        break
                    else:
                        continue
                bags = []
                bag_count = 0     
    return score

if __name__ == "__main__":
    # print(part1("Day 3\\input.txt"))
    # print(part1("Day 3\\example.txt"))
    print(part2("Day 3\\input.txt"))
    print(part2("Day 3\\example.txt"))