import numpy as np

def part1(fileName):
    score = 0
    with open(fileName,"r") as f:
        line = f.readline()
        trees = np.empty((len(line)-1,len(line)-1),dtype=int)
        row = 0
        while line:
            # Code goes here
            line = line.replace("\n","")
            for i in range(len(line)):
                trees[row][i] = int(line[i])
            row = row + 1
            line = f.readline()
    # Add outside trees
    score = score + 2*(row) + 2*(row-2)
    for i in range(1,row-1):
        for j in range(1,row-1):
            look_left = trees[i][j] - trees[i,:j]
            look_right = trees[i][j] - trees[i,j+1:]
            look_up = trees[i][j] - trees[:i,j]
            look_down = trees[i][j] - trees[i+1:,j]
            if min(look_left) > 0 or min(look_right) > 0 or min(look_up) > 0 or min(look_down) > 0:
                score = score + 1                
    return score

def part2(fileName):
    score = 0
    with open(fileName,"r") as f:
        line = f.readline()
        trees = np.empty((len(line)-1,len(line)-1),dtype=int)
        row = 0
        while line:
            # Code goes here
            line = line.replace("\n","")
            for i in range(len(line)):
                trees[row][i] = int(line[i])
            row = row + 1
            line = f.readline()
    # Check scores
    for i in range(1,row-1):
        for j in range(1,row-1):
            tree_score = 1
            look_left = np.flip(trees[i][j] - trees[i,:j])
            look_right = trees[i][j] - trees[i,j+1:]
            look_up = np.flip(trees[i][j] - trees[:i,j])
            look_down = trees[i][j] - trees[i+1:,j]

            # Check Left of tree
            edge = True
            for k in range(len(look_left)):
                if look_left[k] <= 0:
                    tree_score = tree_score*(k+1)
                    edge = False
                    break
            if edge:
                tree_score = tree_score*(k+1)

            # Check Right of tree
            edge = True
            for k in range(len(look_right)):
                if look_right[k] <= 0:
                    tree_score = tree_score*(k+1)
                    edge = False
                    break
            if edge:
                tree_score = tree_score*(k+1)

            # Check Above of tree
            edge = True
            for k in range(len(look_up)):
                if look_up[k] <= 0:
                    tree_score = tree_score*(k+1)
                    edge = False
                    break
            if edge:
                tree_score = tree_score*(k+1)

            # Check below of tree
            edge = True
            for k in range(len(look_down)):
                if look_down[k] <= 0:
                    tree_score = tree_score*(k+1)
                    edge = False
                    break
            if edge:
                tree_score = tree_score*(k+1)

            if tree_score > score:
                score = tree_score
    return score


if __name__ == "__main__":
    day = 8
    # print(part1("Day " + str(day) + "\\example.txt"))
    # print(part1("Day " + str(day) + "\\input.txt"))
    # print(part2("Day " + str(day) + "\\example.txt"))
    print(part2("Day " + str(day) + "\\input.txt"))