import numpy as np

def part1(fileName):
    rock = {}
    lowest_y = 0
    with open(fileName,"r") as f:
        line = f.readline()
        while line:
            # Code goes here
            line = line.replace("\n","")
            points = line.split("->")
            for i in range(len(points)):
                pointx, pointy = points[i].split(",")
                pointx = int(pointx)
                pointy = int(pointy)
                if i == 0:
                    x = pointx
                    y = pointy
                else:
                    if pointx == x:
                        if pointy - y > 0: # Moving Up
                            shift = 0
                        else:   # Moving Down
                            shift = -1*abs(pointy - y)
                        for j in range(abs(pointy-y)+1):
                            rock[str(x) + "," + str( y + j + shift)] = True
                    else:
                        if pointx - x > 0: # Moving Right
                            shift = 0
                        else:   # Moving left
                            shift = -1*abs(pointx - x)
                        for j in range(abs(pointx-x)+1):
                            rock[str(x+ j + shift) + "," + str(y)] = True
                    x = pointx
                    y = pointy
                if y > lowest_y:
                    lowest_y = y
            line = f.readline()
    # Sand Falling
    score = 0
    sandx = 500
    sandy = 0
    while sandy < lowest_y +1:
        if str(sandx) + "," + str(sandy) in rock:
            print("Why you in a rock?")
            break
        while sandy < lowest_y +1: #Falling sand
            if not str(sandx) + "," + str(sandy+1) in rock:
                sandy = sandy + 1
            elif not str(sandx-1) + "," + str(sandy+1) in rock:
                sandx = sandx - 1
                sandy = sandy + 1
            elif not str(sandx+1) + "," + str(sandy+1) in rock:
                sandx = sandx + 1
                sandy = sandy + 1
            else:
                rock[str(sandx) + "," + str(sandy)] = True
                sandx = 500
                sandy = 0
                score = score + 1
                # print(score)
                break
    # print("Stop")
    return score

def part2(fileName):
    rock = {"500,0":False}
    lowest_y = 0
    with open(fileName,"r") as f:
        line = f.readline()
        while line:
            # Code goes here
            line = line.replace("\n","")
            points = line.split("->")
            for i in range(len(points)):
                pointx, pointy = points[i].split(",")
                pointx = int(pointx)
                pointy = int(pointy)
                if i == 0:
                    x = pointx
                    y = pointy
                else:
                    if pointx == x:
                        if pointy - y > 0: # Moving Up
                            shift = 0
                        else:   # Moving Down
                            shift = -1*abs(pointy - y)
                        for j in range(abs(pointy-y)+1):
                            rock[str(x) + "," + str( y + j + shift)] = True
                    else:
                        if pointx - x > 0: # Moving Right
                            shift = 0
                        else:   # Moving left
                            shift = -1*abs(pointx - x)
                        for j in range(abs(pointx-x)+1):
                            rock[str(x+ j + shift) + "," + str(y)] = True
                    x = pointx
                    y = pointy
                if y > lowest_y:
                    lowest_y = y
            line = f.readline()
    # Sand Falling
    score = 0
    sandx = 500
    sandy = 0
    while rock["500,0"] == False:
        if str(sandx) + "," + str(sandy) in rock:
            if not rock[str(x+ j + shift) + "," + str(y)]:
                print("Why you in a rock?")
                break
        while True: #Falling sand
            if sandy == lowest_y + 1:
                break
            if not str(sandx) + "," + str(sandy+1) in rock:
                sandy = sandy + 1
            elif not str(sandx-1) + "," + str(sandy+1) in rock:
                sandx = sandx - 1
                sandy = sandy + 1
            elif not str(sandx+1) + "," + str(sandy+1) in rock:
                sandx = sandx + 1
                sandy = sandy + 1
            else:
                break
        rock[str(sandx) + "," + str(sandy)] = True
        sandx = 500
        sandy = 0
        score = score + 1
    # print("Stop")
    return score



if __name__ == "__main__":
    day = 14
    # print(part1("Day " + str(day) + "\\example.txt"))
    # print(part1("Day " + str(day) + "\\input.txt"))
    # print(part2("Day " + str(day) + "\\example.txt"))
    print(part2("Day " + str(day) + "\\input.txt"))