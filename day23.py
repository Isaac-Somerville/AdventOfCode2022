from math import inf

def makeInput(file):
    with open(file) as f:
        lines = f.readlines()
    
    grid = []
    for x in lines:
        line = list(x.strip())
        grid.append(line)
    
    return grid


def willMove(elf,elves):
    steps = [-1,0,1]
    y,x = elf
    for xStep in steps:
        for yStep in steps:
            if not (xStep == 0 and yStep == 0):
                if (y+yStep,x+xStep) in elves:
                    return True
    return False

def willMoveNorth(elf,elves):
    y,x = elf
    yStep = -1
    xSteps = [-1,0,1]
    for xStep in xSteps:
        if (y+yStep,x+xStep) in elves:
            return elf
    return (y-1,x)

def willMoveSouth(elf,elves):
    y,x = elf
    yStep = 1
    xSteps = [-1,0,1]
    for xStep in xSteps:
        if (y+yStep,x+xStep) in elves:
            return elf
    return (y+1,x)

def willMoveWest(elf,elves):
    y,x = elf
    xStep = -1
    ySteps = [-1,0,1]
    for yStep in ySteps:
        if (y+yStep,x+xStep) in elves:
            return elf
    return (y,x-1)

def willMoveEast(elf,elves):
    y,x = elf
    xStep = 1
    ySteps = [-1,0,1]
    for yStep in ySteps:
        if (y+yStep,x+xStep) in elves:
            return elf
    return (y,x+1)

file = 'day23.txt'
grid  = makeInput(file)
# for row in grid:
#     print(row)
elfSet = set()
elfList = []

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '#':
            elfSet.add((i,j))
            elfList.append((i,j))

dirs = ['N','S','W','E']
moveDict = {'N':willMoveNorth, 'S': willMoveSouth,'W': willMoveWest,'E':willMoveEast}
elvesMoving = True
i = 0
while elvesMoving:
    elvesMoving = False
    newElfSet = set()
    newElfList = []
    for elf in elfList:
        if not willMove(elf, elfSet): #elf's position will not change
            newElfList.append(elf)
            newElfSet.add(elf)
    
    dirOrder = [j % 4 for j in range(i,i+4)]
    #print(dirOrder)
    proposedDict = {}
    for elf in elfList:
        #print(elf)
        if elf not in newElfSet: #elf position will change, check each direction
            elfMoved = False
            for j in dirOrder:
                dirFunc = moveDict[dirs[j]]
                newElf = dirFunc(elf,elfSet)
                if newElf != elf:
                    if newElf in proposedDict:
                        proposedDict[newElf].append(elf)
                    else:
                        proposedDict[newElf] = [elf]
                    elfMoved = True
                    break
            if not elfMoved:
                newElfList.append(elf)
                newElfSet.add(elf)

    

    for newElf in proposedDict:
        if len(proposedDict[newElf]) > 1: #multiple elves proposed same location, no elves move
            newElfList += proposedDict[newElf]
            newElfSet.update(proposedDict[newElf])
        else:
            elvesMoving = True
            newElfList.append(newElf)
            newElfSet.add(newElf)
    
    elfSet = newElfSet
    elfList = newElfList
    i += 1

xMax = yMax = -inf
xMin = yMin = inf

for elf in elfList:
    yMin = min(yMin,elf[0])
    yMax = max(yMax,elf[0])
    xMin = min(xMin,elf[1])
    xMax = max(xMax,elf[1])

print((yMax-yMin + 1) * (xMax-xMin + 1))
print((yMax-yMin + 1) * (xMax-xMin + 1) - len(elfList))
print(i)
