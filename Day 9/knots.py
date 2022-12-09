import numpy as np

def away(H,T):
    if abs(H[0]-T[0]) > 1:
        return (True)
    elif abs(H[1]-T[1]) > 1:
        return(True)
    else:
        return False

def part1(fileName):
    score = 0
    line_count = 0
    grid = np.zeros((1000,1000),dtype=int)
    grid[500,500] = 1
    H = [500,500]
    T = [500,500]
    with open(fileName,"r") as f:
        line = f.readline()
        while line:
            line_count = line_count + 1
            # print(np.sum(np.sum(grid)))
            # Code goes here
            line = line.replace("\n","").split(" ")
            direction = line[0]
            steps = int(line[1])

            for step in range(steps):
                match direction:
                    case "U":
                        H[0] = H[0]-1
                    case "D":
                        H[0] = H[0]+1
                    case "L":
                        H[1] = H[1]-1
                    case "R":
                        H[1] = H[1]+1

                if away(H,T):
                    if H[0] == T[0]: # Same Row
                        if H[1] > T[1]: # To the right
                           T[1] = T[1]+1
                        else: #To the left
                            T[1] = T[1]-1
                         
                    elif H[1] == T[1]: # Same Column
                        if H[0] > T[0]: # Under
                           T[0] = T[0]+1
                        else: #Above
                            T[0] = T[0]-1
                    else:
                        if abs(H[0] - T[0]) > abs(H[1] - T[1]): # Further vertical
                            if H[0] > T[0]: # heads under tails
                                T[0] = T[0] + 1
                            else:
                                T[0] = T[0] - 1
                            T[1] = H[1]
                        else: #Further Horizonatl
                            if H[1] > T[1]: # heads right of tails
                                T[1] = T[1] + 1
                            else:
                                T[1] = T[1] - 1
                            T[0] = H[0]
                    # Update grid
                    grid[T[0],T[1]] = 1
            line = f.readline()
    score = np.sum(np.sum(grid))
    return score


def part2(fileName):
    score = 0
    line_count = 0
    knots = []
    # Example
    # grid = np.zeros((26,26),dtype=int)
    # grid[15,11] = 1
    # for i in range(10):
    #     knots.append([15,11])
    # Input
    grid = np.zeros((1000,1000),dtype=int)
    grid[100,100] = 1
    for i in range(10):
        knots.append([100,100])
    with open(fileName,"r") as f:
        line = f.readline()
        while line:
            line_count = line_count + 1
            # print(np.sum(np.sum(grid)))
            line = line.replace("\n","").split(" ")
            direction = line[0]
            steps = int(line[1])

            for step in range(steps):
                count = np.sum(np.sum(grid))
                match direction:
                    case "U":
                        knots[0][0] = knots[0][0]-1
                    case "D":
                        knots[0][0] = knots[0][0]+1
                    case "L":
                        knots[0][1] = knots[0][1]-1
                    case "R":
                        knots[0][1] = knots[0][1]+1
                for i in range(1,10):
                    while away(knots[i-1],knots[i]):
                        if knots[i-1][0] == knots[i][0]: # Same Row
                            if knots[i-1][1] > knots[i][1]: # To the right
                                knots[i][1] = knots[i][1]+1
                            else: #To the left
                                knots[i][1] = knots[i][1]-1
                            
                        elif knots[i-1][1] == knots[i][1]: # Same Column
                            if knots[i-1][0] > knots[i][0]: # Under
                                knots[i][0] = knots[i][0]+1
                            else: #Above
                                knots[i][0] = knots[i][0]-1
                        else:
                            if knots[i-1][0] > knots[i][0]:
                                knots[i][0] = knots[i][0] + 1
                            else:
                                knots[i][0] = knots[i][0] - 1
                            
                            if knots[i-1][1] > knots[i][1]:
                                knots[i][1] = knots[i][1] + 1
                            else:
                                knots[i][1] = knots[i][1] - 1
                        # Update grid
                        grid[knots[-1][0],knots[-1][1]] = 1
            line = f.readline()
    score = np.sum(np.sum(grid))
    return score

if __name__ == "__main__":
    day = 9
    # print(part1("Day " + str(day) + "\\example.txt"))
    # print(part1("Day " + str(day) + "\\input.txt"))
    print(part2("Day " + str(day) + "\\example2.txt"))
    print(part2("Day " + str(day) + "\\input.txt"))