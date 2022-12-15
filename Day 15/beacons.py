
# https://datagy.io/manhattan-distance-python/
# Calculating Manhattan Distance from Scratch
def manhattan_distance(point1, point2):
    return sum(abs(int(value1) - int(value2)) for value1, value2 in zip(point1, point2))

def part1(fileName, row):
    score = 0
    blocked = {}
    beacons = {}
    # min_x =  9999999
    # max_x = -9999999
    with open(fileName,"r") as f:
        line = f.readline()
        while line:
            # Code goes here
            coord = line.replace("\n","").replace("Sensor at x=","").replace(" closest beacon is at x=","").replace(" y=","")
            sensor, beacon = coord.split(":")
            sensorx, sensory = sensor.split(",")
            beaconx, beacony = beacon.split(",")

            distance = manhattan_distance((sensorx, sensory), (beaconx, beacony))
            if int(sensory) + distance >= row or int(sensory) - distance <= row:
                row_distance = distance - abs(int(sensory) - row)
                for i in range(row_distance+1):
                    blocked[str(int(sensorx)+i)] = True
                    blocked[str(int(sensorx)-i)] = True
            if int(beacony) == row:
                beacons[beaconx] = True

            # sensors[sensorx + "," + sensory] = [(int(sensorx), int(sensory)),
            #                                     manhattan_distance((sensorx, sensory), (beaconx, beacony))]
            # beacons[beaconx + "," + beacony] = True
            
            # if int(sensorx) < min_x:
            #     min_x = int(sensorx)
            # elif int(sensorx) > max_x:
            #     max_x = int(sensorx)
            
            # if int(beaconx) < min_x:
            #     min_x = int(beaconx)
            # elif int(beaconx) > max_x:
            #     max_x = int(beaconx)
            line = f.readline()
    #Check row
    # y = 2000000
    # for x in range(min_x,max_x + 2):
    #     print(x)
    #     found = False
    #     if str(x) + "," + str(y) in beacons:
    #         continue

    #     for sensor in sensors:
    #         if manhattan_distance(sensors[sensor][0],(x,y)) <= sensors[sensor][1]:
    #             found = True
    #             break

    #     if found:
    #         score = score + 1
    for x in list(blocked.keys()):
        if x in beacons:
            blocked.pop(x)
    score = len(blocked)
    return score


def within_sensor(sensors, point):
    for sensor in sensors:
        if manhattan_distance(point, sensors[sensor][0]) <= sensors[sensor][1]:
            return True
    return False
        

def part2(fileName, search_size):
    sensors = {}
    with open(fileName,"r") as f:
        line = f.readline()
        while line:
            # Code goes here
            coord = line.replace("\n","").replace("Sensor at x=","").replace(" closest beacon is at x=","").replace(" y=","")
            sensor, beacon = coord.split(":")
            sensorx, sensory = sensor.split(",")
            beaconx, beacony = beacon.split(",")
            
            sensors[sensorx + "," + sensory] = [(int(sensorx), int(sensory)),
                                            manhattan_distance((sensorx, sensory), (beaconx, beacony))]
            line = f.readline()

    overlap = True
    for sensor in sensors:
        x_max = sensors[sensor][0][0]+sensors[sensor][1]+1
        x_min = sensors[sensor][0][0]-sensors[sensor][1]-1
        y_max = sensors[sensor][0][1]+sensors[sensor][1]+1
        y_min = sensors[sensor][0][1]-sensors[sensor][1]-1
        distance = sensors[sensor][1]
        #Start at the top
        x = sensors[sensor][0][0]
        y = y_min
        # Go down right
        while x <= x_max and overlap:
            if (0 <= x <= search_size) and (0 <= y <= search_size):
                if not within_sensor(sensors, (x,y)):
                    overlap = False
                    print("{},{}".format(x,y))
                    score = x*4000000+y
                    break
            x = x + 1
            y = y + 1
        
        #Start at the Right
        x = x_max
        y = sensors[sensor][0][1]
        # Go down Left
        while y <= y_max and overlap:
            if (0 <= x <= search_size) and (0 <= y <= search_size):
                if not within_sensor(sensors, (x,y)):
                    overlap = False
                    print("{},{}".format(x,y))
                    score = x*4000000+y
                    break
            x = x - 1
            y = y + 1
        
        #Start at the Bottom
        x = sensors[sensor][0][0]
        y = y_max
        # Go down Left
        while x >= x_min and overlap:
            if (0 <= x <= search_size) and (0 <= y <= search_size):
                if not within_sensor(sensors, (x,y)):
                    overlap = False
                    print("{},{}".format(x,y))
                    score = x*4000000+y
                    break
            x = x - 1
            y = y - 1
        
        #Start at the Left
        x = x_min
        y = sensors[sensor][0][1]
        # Go down Left
        while y >= y_min and overlap:
            if (0 <= x <= search_size) and (0 <= y <= search_size):
                if not within_sensor(sensors, (x,y)):
                    overlap = False
                    print("{},{}".format(x,y))
                    score = x*4000000+y
                    break
            x = x + 1
            y = y - 1

        if not overlap:
            break
    return score


if __name__ == "__main__":
    day = 15
    # print(part1("Day " + str(day) + "\\example.txt",10))
    # print(part1("Day " + str(day) + "\\input.txt",2000000))
    # print(part2("Day " + str(day) + "\\example.txt",20))
    print(part2("Day " + str(day) + "\\input.txt",4000000))