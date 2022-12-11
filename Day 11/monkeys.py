

def part1(fileName):
    score = 0
    # monkeys = [
    #     {
    #     "N" : 0,
    #     "Operation": ["*",19],
    #     "Test": 23,
    #     "True": 2,
    #     "False":3,
    #     "Items":[],
    #     "Inspections" : 0
    # },{
    #     "N" : 1,
    #     "Operation": ["+",6],
    #     "Test": 19,
    #     "True": 2,
    #     "False":0,
    #     "Items":[],
    #     "Inspections" : 0
    # },{
    #     "N" : 2,
    #     "Operation": ["**",2],
    #     "Test": 13,
    #     "True": 1,
    #     "False":3,
    #     "Items":[],
    #     "Inspections" : 0
    # },{
    #     "N" : 3,
    #     "Operation": ["+",3],
    #     "Test": 17,
    #     "True": 0,
    #     "False":1,
    #     "Items":[],
    #     "Inspections" : 0
    # }]

    monkeys = [
        {
        "N" : 0,
        "Operation": ["*",7],
        "Test": 13,
        "True": 1,
        "False":3,
        "Items":[],
        "Inspections" : 0
    },
    {
        "N" : 1,
        "Operation": ["+",7],
        "Test": 19,
        "True": 2,
        "False":7,
        "Items":[],
        "Inspections" : 0
    },
    {
        "N" : 2,
        "Operation": ["*",3],
        "Test": 5,
        "True": 5,
        "False":7,
        "Items":[],
        "Inspections" : 0
    },
    {
        "N" : 3,
        "Operation": ["+",3],
        "Test": 2,
        "True": 1,
        "False":2,
        "Items":[],
        "Inspections" : 0
    },
    {
        "N" : 4,
        "Operation": ["**",2],
        "Test": 17,
        "True": 6,
        "False":0,
        "Items":[],
        "Inspections" : 0
    },
    {
        "N" : 5,
        "Operation": ["+",8],
        "Test": 11,
        "True": 4,
        "False":6,
        "Items":[],
        "Inspections" : 0
    },
    {
        "N" : 6,
        "Operation": ["+",2],
        "Test": 7,
        "True": 3,
        "False":0,
        "Items":[],
        "Inspections" : 0
    },
    {
        "N" : 7,
        "Operation": ["+",4],
        "Test": 3,
        "True": 4,
        "False":5,
        "Items":[],
        "Inspections" : 0
    }]
    with open(fileName,"r") as f:
        line = f.readline()
        count = 0
        while line:
            # Code goes here
            
            line = line.replace("\n","")
            if "Starting items" in line:
                line = line.strip().replace("Starting items: ","").split(",")
                for item in line:
                    monkeys[count]["Items"].append(int(item))
                count = count + 1
            line = f.readline()

    # Do Rounds
    round = 0
    while round < 20:
        for monkey in monkeys:
            while len(monkey["Items"]) != 0:
                item = monkey["Items"][0]
                match monkey["Operation"][0]:
                    case "*":
                        item = item*monkey["Operation"][1]
                    case "**":
                        item = item**monkey["Operation"][1]
                    case "+":
                        item = item+monkey["Operation"][1]
                monkey["Inspections"] = monkey["Inspections"] + 1
                item = int(item/3)
                if item%monkey["Test"] == 0:
                    monkeys[monkey["True"]]["Items"].append(item)
                else:
                    monkeys[monkey["False"]]["Items"].append(item)
                monkey["Items"].pop(0)
        round = round + 1
    print("After 20 rounds")
    inspections = []
    for monkey in monkeys:
        inspections.append(monkey["Inspections"])
    inspections = sorted(inspections)
    score = inspections[-1]*inspections[-2]
    return score

import math
def part2(fileName):
    score = 0
    # monkeys = [
    #     {
    #     "N" : 0,
    #     "Operation": ["*",19],
    #     "Test": 23,
    #     "True": 2,
    #     "False":3,
    #     "Items":[],
    #     "Inspections" : 0
    # },{
    #     "N" : 1,
    #     "Operation": ["+",6],
    #     "Test": 19,
    #     "True": 2,
    #     "False":0,
    #     "Items":[],
    #     "Inspections" : 0
    # },{
    #     "N" : 2,
    #     "Operation": ["**",2],
    #     "Test": 13,
    #     "True": 1,
    #     "False":3,
    #     "Items":[],
    #     "Inspections" : 0
    # },{
    #     "N" : 3,
    #     "Operation": ["+",3],
    #     "Test": 17,
    #     "True": 0,
    #     "False":1,
    #     "Items":[],
    #     "Inspections" : 0
    # }]

    monkeys = [
        {
        "N" : 0,
        "Operation": ["*",7],
        "Test": 13,
        "True": 1,
        "False":3,
        "Items":[],
        "Inspections" : 0
    },
    {
        "N" : 1,
        "Operation": ["+",7],
        "Test": 19,
        "True": 2,
        "False":7,
        "Items":[],
        "Inspections" : 0
    },
    {
        "N" : 2,
        "Operation": ["*",3],
        "Test": 5,
        "True": 5,
        "False":7,
        "Items":[],
        "Inspections" : 0
    },
    {
        "N" : 3,
        "Operation": ["+",3],
        "Test": 2,
        "True": 1,
        "False":2,
        "Items":[],
        "Inspections" : 0
    },
    {
        "N" : 4,
        "Operation": ["**",2],
        "Test": 17,
        "True": 6,
        "False":0,
        "Items":[],
        "Inspections" : 0
    },
    {
        "N" : 5,
        "Operation": ["+",8],
        "Test": 11,
        "True": 4,
        "False":6,
        "Items":[],
        "Inspections" : 0
    },
    {
        "N" : 6,
        "Operation": ["+",2],
        "Test": 7,
        "True": 3,
        "False":0,
        "Items":[],
        "Inspections" : 0
    },
    {
        "N" : 7,
        "Operation": ["+",4],
        "Test": 3,
        "True": 4,
        "False":5,
        "Items":[],
        "Inspections" : 0
    }]
    with open(fileName,"r") as f:
        line = f.readline()
        count = 0
        while line:
            # Code goes here
            
            line = line.replace("\n","")
            if "Starting items" in line:
                line = line.strip().replace("Starting items: ","").split(",")
                for item in line:
                    monkeys[count]["Items"].append(int(item))
                count = count + 1
            line = f.readline()

    # Do Rounds
    reducer = math.lcm(*[monkey["Test"] for monkey in monkeys])
    round = 0
    while round < 10000:
        for monkey in monkeys:
            while len(monkey["Items"]) != 0:
                item = monkey["Items"][0]
                match monkey["Operation"][0]:
                    case "*":
                        item = item*monkey["Operation"][1]
                    case "**":
                        item = item**monkey["Operation"][1]
                    case "+":
                        item = item+monkey["Operation"][1]
                monkey["Inspections"] = monkey["Inspections"] + 1
                # item = int(item/3)
                item = item%reducer
                if item%monkey["Test"] == 0:
                    monkeys[monkey["True"]]["Items"].append(item)
                else:
                    monkeys[monkey["False"]]["Items"].append(item)
                monkey["Items"].pop(0)
        round = round + 1
    print("After 10000 rounds")
    inspections = []
    for monkey in monkeys:
        inspections.append(monkey["Inspections"])
    inspections = sorted(inspections)
    score = inspections[-1]*inspections[-2]
    return score



if __name__ == "__main__":
    day = 11
    # print(part1("Day " + str(day) + "\\example.txt"))
    # print(part1("Day " + str(day) + "\\input.txt"))
    # print(part2("Day " + str(day) + "\\example.txt"))
    print(part2("Day " + str(day) + "\\input.txt"))