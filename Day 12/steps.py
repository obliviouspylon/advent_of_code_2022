import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
from collections import deque

grid = []

#Depth Wise Search attempt
# def distance(point1, point2):
#     return(((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5)
# def tryPath(end_point, current, previous, steps, fig, colour_grid):
#     global score
#     global grid
#     # print(str(current) + " " + str(grid[current[0]][current[1]]))
#     if current == end_point:
#         if steps < score:
#             score = steps
#         print("Found End " + str(steps))
#         return (True)

#     x = current[0]
#     y = current[1]

#     paths = []
#     if x != 0:
#         if (grid[x-1][y] - grid[x][y] == 1 or grid[x-1][y] - grid[x][y] == 0) and [x-1,y] != previous:
#             paths.append({
#                 "direction": "up",
#                 "point": [x-1,y],
#                 "distance" : distance([x-1,y], end_point)
#             })
    
#     if x != (len(grid)-1):
#         if (grid[x+1][y] - grid[x][y] == 1 or grid[x+1][y] - grid[x][y] == 0) and [x+1,y] != previous:
#             paths.append({
#                 "direction": "down",
#                 "point": [x+1,y],
#                 "distance" : distance([x+1,y], end_point)
#             })
    
#     if y != 0:
#         if (grid[x][y-1] - grid[x][y] == 1 or grid[x][y-1] - grid[x][y] == 0) and [x,y-1] != previous:
#             paths.append({
#                 "direction": "left",
#                 "point": [x,y-1],
#                 "distance" : distance([x,y-1], end_point)
#             })

#     if y != (len(grid[0])-1):
#         if (grid[x][y+1] - grid[x][y] == 1 or grid[x][y+1] - grid[x][y] == 0) and [x,y+1] != previous:
#             paths.append({
#                 "direction": "right",
#                 "point": [x,y+1],
#                 "distance" : distance([x,y+1], end_point)
#             })

#     grid[x][y] = -1
#     sorted_paths = sorted(paths,key = lambda path: path["distance"])

#     colour_grid.set_data(np.array(grid))
#     fig.canvas.draw()
#     fig.canvas.flush_events()

#     for path in sorted_paths:
#         if grid[path["point"][0]][path["point"][1]] != -1:
#             result = tryPath(end_point, path["point"], current, steps+1, fig, colour_grid)
#             if result:
#                 return(True)
#         else:
#             continue

#     return(False)


# Breath wise search attempt
def validStep(point1,point2):
    global grid
    x1,y1 = point1
    x2,y2 = point2
    if ord(grid[x2][y2]) - ord(grid[x1][y1]) <= 1:
        return True
    else:
        return False

def part1(fileName):
    global grid
    with open(fileName,"r") as f:
        line = f.readline()
        row_count = 0
        while line:
            # Code goes here
            row = []
            line = line.replace("\n","")
            for i in range(len(line)):
                if line[i] == "S":
                    start_point = [row_count,i]
                    row.append("a")
                elif line[i] == "E":
                    end_point = [row_count,i]
                    row.append("z")
                else:
                    row.append(line[i])
            grid.append(row)
            row = []
            row_count = row_count +1
            line = f.readline()
    # Find path using recusion

    grid = np.array(grid)
    #Depth Wise Search attempt
    # tryPath(end_point, start_point, [-1,-1], 0, fig, colour_grid)

    #Breath Wise Search attempt
    points = deque([])
    vistied = {
        str(start_point[0]) + "," + str(start_point[1]) : True
    }
    seen = {}

    for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
        if (0 <= start_point[0]+x < grid.shape[0] and 0 <= start_point[0]+y < grid.shape[1]):
            if validStep(start_point,[start_point[0]+x,start_point[1]+y]):
                points.append({
                    "point" : [start_point[0]+x,start_point[1]+y],
                    "steps" : 1,
                    # "distance": distance([start_point[0]+x,start_point[1]+y],end_point)
                })
                seen[str(start_point[0]) + "," + str(start_point[1])] = True

    found = False
    while len(points) > 0 and not found:
        # points = sorted(points, key = lambda point: point["steps"])

        x = points[0]["point"][0]
        y = points[0]["point"][1]
        steps = points[0]["steps"]
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            if (0 <= x+dx < grid.shape[0] and 0 <= y+dy < grid.shape[1]):
                if not str(x+dx) + "," + str(y+dy) in vistied and not str(x+dx) + "," + str(y+dy) in seen:
                    if validStep([x,y], [x+dx, y+dy]):
                        if [x+dx, y+dy] == end_point:
                            score = (steps + 1)
                            found = True
                            break
                        else:
                            points.append({
                                "point" : [x+dx,y+dy],
                                "steps" : steps + 1,
                                # "distance": distance([x+dx,y+dy],end_point)
                            })
                            seen[str(x+dx) + "," + str(y+dy)] = True
        
        vistied[str(x) + "," + str(y)] = True
        points.popleft()


    return (score)

def part2(fileName):
    global grid
    with open(fileName,"r") as f:
        line = f.readline()
        row_count = 0
        while line:
            # Code goes here
            row = []
            line = line.replace("\n","")
            for i in range(len(line)):
                if line[i] == "S":
                    start_point = [row_count,i]
                    row.append("a")
                elif line[i] == "E":
                    end_point = [row_count,i]
                    row.append("z")
                else:
                    row.append(line[i])
            grid.append(row)
            row = []
            row_count = row_count +1
            line = f.readline()
    # Find path using recusion

    grid = np.array(grid)
    #Depth Wise Search attempt
    # tryPath(end_point, start_point, [-1,-1], 0, fig, colour_grid)

    #Breath Wise Search attempt
    points = deque([])
    vistied = {
        str(end_point[0]) + "," + str(end_point[1]) : True
    }
    seen = {}

    for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
        if (0 <= end_point[0]+x < grid.shape[0] and 0 <= end_point[0]+y < grid.shape[1]):
            if validStep([end_point[0]+x,end_point[1]+y],end_point):
                points.append({
                    "point" : [end_point[0]+x,end_point[1]+y],
                    "steps" : 1,
                    # "distance": distance([start_point[0]+x,start_point[1]+y],end_point)
                })
                seen[str(end_point[0]) + "," + str(end_point[1])] = True

    found = False
    while len(points) > 0 and not found:
        # points = sorted(points, key = lambda point: point["steps"])

        x = points[0]["point"][0]
        y = points[0]["point"][1]
        steps = points[0]["steps"]
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            if (0 <= x+dx < grid.shape[0] and 0 <= y+dy < grid.shape[1]):
                if not str(x+dx) + "," + str(y+dy) in vistied and not str(x+dx) + "," + str(y+dy) in seen:
                    if validStep( [x+dx, y+dy],[x,y]):
                        if grid[x+dx, y+dy] == "a":
                            score = (steps + 1)
                            found = True
                            break
                        else:
                            points.append({
                                "point" : [x+dx,y+dy],
                                "steps" : steps + 1,
                                # "distance": distance([x+dx,y+dy],end_point)
                            })
                            seen[str(x+dx) + "," + str(y+dy)] = True
        
        vistied[str(x) + "," + str(y)] = True
        points.popleft()


    return (score)


if __name__ == "__main__":
    day = 12
    # print(part1("Day " + str(day) + "\\example.txt"))
    # print(part1("Day " + str(day) + "\\input.txt"))
    # print(part2("Day " + str(day) + "\\example.txt"))
    print(part2("Day " + str(day) + "\\input.txt"))