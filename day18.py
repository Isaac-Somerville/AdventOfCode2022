def makeInput(file):
    with open(file) as f:
        lines = f.readlines()
    
    input = []
    for x in lines:
        temp = x.strip().split(',')
        line = [int(y) for y in temp]
        input.append(line)

    return input

file = 'day18test.txt'
inputLst = makeInput(file)
xMax = max([input[0] for input in inputLst])
yMax = max([input[1] for input in inputLst])
zMax = max([input[2] for input in inputLst])
inputTups = [tuple(x) for x in inputLst]
lava = set(inputTups)
print(inputLst)
print(inputTups)
print(lava)

totalSides  = 0
for cube in inputLst:
    sides = 6
    adj = [-1,1]
    for move in adj:
        for i in range(3):
            neighbour = [x for x in cube]
            neighbour[i] += move
            tupNbr = tuple(neighbour)
            if tupNbr in lava:
                #print(cube,neighbour)
                sides -= 1
    totalSides += sides

print(totalSides)

airLst = []
for x in range(xMax):
    for y in range(yMax):
        for z in range(zMax):
            if (x,y,z) not in lava:
                airLst.append([x,y,z])

airTups = [tuple(air) for air in airLst]
airSet = set(airTups)

def findInsideAir(airLst,airSet,lava,xMax,yMax,zMax):
    outsideAir = set()
    for current in airLst:
        foundOutside = False
        queue = [current]
        visited = {tuple(current)}
        while queue:
            newQueue = []
            for i in range(len(queue)):
                cube = queue[i]
                adj = [-1,1]
                for move in adj:
                    for i in range(3):
                        neighbour = [x for x in cube]
                        neighbour[i] += move
                        tupNbr = tuple(neighbour)
                        if tupNbr not in visited and tupNbr not in lava:
                            if neighbour[0] == xMax or neighbour[1] == yMax or neighbour[2] == zMax:
                                foundOutside = True
                            else:
                                newQueue.append(neighbour)
                                visited.add(tupNbr)
            queue = newQueue
            if foundOutside:
                outsideAir.add(tuple(current))
                break
    return airSet - outsideAir

insideAirSet = findInsideAir(airLst,airSet,lava,xMax,yMax,zMax)
temp = list(insideAirSet)
insideAirLst = [list(x) for x in temp]

airSides = 0
for air in insideAirLst:
    sides = 6
    adj = [-1,1]
    for move in adj:
        for i in range(3):
            neighbour = [x for x in air]
            neighbour[i] += move
            tupNbr = tuple(neighbour)
            if tupNbr in insideAirSet:
                #print(cube,neighbour)
                sides -= 1
    airSides += sides

print(totalSides - airSides)
# 2588!
                

