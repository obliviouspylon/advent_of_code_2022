import re

def filePath(path):
    pathString = ""
    for i in path:
        if i != "/":
            pathString = pathString + "/" + i
    return(pathString)

def part1(fileName):
    score = 0
    path = []
    files = {}
    folders = []
    with open(fileName,"r") as f:
        line = f.readline()
        while line:
            # Code goes here
            line = line.replace("\n","")
            if line[0] == "$":
                # print("Action")
                if line[2:4] == "cd":
                    # print("Change Folder")
                    if line == "$ cd ..":
                        path.pop()
                    else:
                        path.append(line[5:])
                elif line[2:4] == "ls":
                    pass
            else:
                # print("Folder Contents")
                if line[:3] == "dir":
                    pathString = filePath(path)
                    folders.append(pathString + "/" + line[4:])
                else:
                    file = line.split(" ")
                    pathString = filePath(path)
                    files[pathString+ ";" +file[1]] = file[0]
            line = f.readline()
    
    for folder in folders:
        folderSize = 0
        for file in list(files.keys()):
            regex = re.compile(folder + ".*;")
            # if folder + ";" in file:
            if re.match(regex, file):
                # print("Pass: " + folder + ".." + file)
                folderSize = folderSize + int(files[file])
            # else:
                # print("Fail: " + folder + ".." + file)
        if folderSize <= 100000:
            score = score + folderSize

    # print("Done")
    return score

def part2(fileName):
    score = 0
    path = []
    files = {}
    folders = {}
    with open(fileName,"r") as f:
        line = f.readline()
        while line:
            # Code goes here
            line = line.replace("\n","")
            if line[0] == "$":
                # print("Action")
                if line[2:4] == "cd":
                    # print("Change Folder")
                    if line == "$ cd ..":
                        path.pop()
                    else:
                        path.append(line[5:])
                elif line[2:4] == "ls":
                    pass
            else:
                # print("Folder Contents")
                if line[:3] == "dir":
                    pathString = filePath(path)
                    folders[pathString + "/" + line[4:]] = 0
                else:
                    file = line.split(" ")
                    pathString = filePath(path)
                    files[pathString+ ";" +file[1]] = file[0]
            line = f.readline()
    

    for folder in folders:
        folderSize = 0
        for file in list(files.keys()):
            regex = re.compile(folder + ".*;")
            # if folder + ";" in file:
            if re.match(regex, file):
                # print("Pass: " + folder + ".." + file)
                folderSize = folderSize + int(files[file])
            # else:
                # print("Fail: " + folder + ".." + file)
        folders[folder] = folderSize

    sizes = list(folders.values())
    sizes = sorted(sizes)

    for size in sizes:
        if size > 8381165:
            score = size
            break

    # print("Done")
    return score

if __name__ == "__main__":
    day = 7
    # print(part1("Day " + str(day) + "\\input.txt"))
    # print(part1("Day " + str(day) + "\\example.txt"))
    # print(part2("Day " + str(day) + "\\input.txt"))
    # print(part2("Day " + str(day) + "\\example.txt"))