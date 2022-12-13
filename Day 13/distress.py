import ast
from collections import deque

def comapre_lists(list_L,list_R):
    list_L = deque(list_L)
    list_R = deque(list_R)
    while len(list_L) > 0 and len(list_R) > 0:
        l1 = list_L[0]
        l2 = list_R[0]
        if list_L[0] == list_R[0]:
            pass
        elif type(list_L[0]) == type(list_R[0]):
            if isinstance(list_L[0], int):
                # Int
                if list_L[0] > list_R[0]:
                    return False
                elif list_L[0] < list_R[0]:
                    return True
                else:
                    pass
            else:
                #List
                result = comapre_lists(list_L[0],list_R[0])
                match result:
                    case False:
                        return False
                    case True:
                        return True
                    case _:
                        pass
        else:
            # Not Equal
            if isinstance(list_L[0], int):
                list1 = [list_L[0]]
                list2 = list_R[0]
            else:
                list1 = list_L[0]
                list2 = [list_R[0]]
            result = comapre_lists(list1,list2)
            match result:
                case False:
                    return False
                case True:
                    return True
                case _:
                    pass
        list_L.popleft()
        list_R.popleft()
    if len(list_L) ==  0 and len(list_R) ==  0:
        return None
    elif len(list_L) ==  0:
        return True
    else:
        return False

def part1(fileName):
    score = 0
    pairs = deque([])
    with open(fileName,"r") as f:
        line = f.readline()
        row = deque([])
        while line:
            # Code goes here
            if line == "\n":
                pairs.append(row)
                row= []
            else:
                row.append(ast.literal_eval(line.replace("\n","")))
            line = f.readline()
        pairs.append(row)
    for i in range(len(pairs)):

        result = comapre_lists(pairs[i][0],pairs[i][1])
        print("Pair " + str(i+1) + ": " + str(result))
        if result:
            score = score + (i+1)
    return score

def part2(fileName):
    score = 1
    pairs = deque([])
    with open(fileName,"r") as f:
        line = f.readline()
        row = deque([])
        while line:
            # Code goes here
            if line == "\n":
                pass
            else:
                pairs.append(ast.literal_eval(line.replace("\n","")))
            line = f.readline()
        pairs.append(ast.literal_eval("[[2]]"))
        pairs.append(ast.literal_eval("[[6]]"))
    
    #Insertion Sort
    i = 1
    while i < (len(pairs)):
        print(i)
        result = comapre_lists(pairs[i-1],pairs[i])
        if result:
            i = i +1
        else:
            j = i
            while True:
                holder = pairs[j]
                pairs.remove(holder)
                pairs.insert(j-1,holder)
                if comapre_lists(pairs[j-1],pairs[j]):
                    i = 1
                    break
                else:
                    j = j -1
    score = score * (pairs.index(ast.literal_eval("[[2]]"))+1)
    score = score * (pairs.index(ast.literal_eval("[[6]]"))+1)
    return score


if __name__ == "__main__":
    day = 13
    # print(part1("Day " + str(day) + "\\example.txt"))
    # print(part1("Day " + str(day) + "\\input.txt"))
    # print(part2("Day " + str(day) + "\\example.txt"))
    print(part2("Day " + str(day) + "\\input.txt"))