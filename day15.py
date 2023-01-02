with open('day15.txt') as f:
    lines = f.readlines()

sensorDict = {}
xMax = xMin = yMax = yMin = 0
sensorLst = []
for x in lines:
    line = x.strip()
    i = 0
    lst = []
    while i <len(line):
        if line[i] == '=':
            i += 1
            temp = ''
            while i < len(line) and line[i] not in {',', ':'}:
                temp += line[i]
                i += 1
            lst.append(int(temp))
        i += 1
    xMax = max(xMax, lst[0],lst[2])
    xMin = min(xMin,lst[0],lst[2])
    yMax = max(yMax,lst[1],lst[3])
    yMin = min(yMin,lst[1],lst[3])
    sensorLst.append(lst)

print(xMax,xMin,yMax,yMin)

for lst in sensorLst:
    sensorDict[(lst[1],lst[0] )] = (lst[3] ,lst[2])         

print(sensorDict)

def distance(tup1,tup2):
    return abs(tup1[0] - tup2[0]) + abs(tup1[1] - tup2[1])

#(x1-x0)y + (y1-y0)x = c

def yInt(y1,x1,y2,x2):
    return int(y1 - (y2-y1)*x1/(x2-x1))

xlim = ylim = 4000000

toCheck = set()
for sensor in sensorDict:
    boundaryDist = distance(sensor,sensorDict[sensor]) + 1
    print(sensor,boundaryDist)
    points = [[sensor[0] - boundaryDist, sensor[1]], [sensor[0], sensor[1] - boundaryDist],
        [sensor[0] + boundaryDist, sensor[1]], [sensor[0], sensor[1] + boundaryDist]]
    for i in range(4):
        if points[i][1] > points[(i+1)%4][1]:
            y1, x1 = points[(i+1) % 4]
            y2, x2 = points[i]
        else:
            y1, x1 = points[i]
            y2, x2 = points[(i+1) % 4]
        m = round((y2-y1)/(x2-x1))
        # print("m=",m)
        c = yInt(y1,x1,y2,x2)
        # print("c=",c)
        for x in range(max(0,x1),min(x2,xlim)+1):
            y = m * x + c
            if 0 <= y <= ylim:
                toCheck.add((y,x))

checkList = list(toCheck)
print("checklist has length", len(checkList))

distDict = {}
for sensor in sensorDict:
    distDict[sensor] = distance(sensor, sensorDict[sensor])

for i in range(len(checkList)):
    print(i)
    point = checkList[i]
    found = True
    for sensor in sensorDict:
        if distance(point,sensor) <= distDict[sensor]:
            found = False
            break
    if found:
        print("point is,",point)
        break

print( 4000000 * 3267801 + 2703981)








# xlim = ylim = 4000000
# xRange = [i for i in range(xlim)]
# for y in range(ylim+1):
#     impossibles = set()
#     for sensor in sensorDict:
#         beacon = sensorDict[sensor]
#         SBDist = distance(sensor,beacon)
#         yDist = abs(y - sensor[0])
#         if yDist <= SBDist:
#             xDist = SBDist - yDist
#             newImpossibles = [sensor[1] + i for i in range(-min(sensor[1], xDist), min(xlim - sensor[1], xDist) + 1)]
#             impossibles.update(newImpossibles)
#         if len(impossibles) >= xlim + 1:
#             break
#     if len(impossibles) < xlim + 1:
#         print(y)
#         print(set(xRange)- impossibles)
#         break
#     print(y)





# y = 2000000
# rowY = set()
# for sensor in sensorDict:
#     beacon = sensorDict[sensor]
#     dist = distance(sensor,beacon)
    
#     tup = (y,beacon[1])
#     while distance(tup, sensor) <= dist:
#         rowY.add(tup)
#         tup = (y,beacon[1]+1)

#     tup = (y,beacon[1]-1)
#     while distance(tup, sensor) <= dist:
#         rowY.add(tup)
#         tup = (y,beacon[1]-1)

# print(len(rowY))


#NOT 5114987

# grid = [['.' for j in range(xMax-xMin +1)] for i in range(yMax-yMin+1)]
# n = len(grid)
# m = len(grid[0])
#print(n,m)

# for (i,j) in sensorDict:
#     print((i,j))
#     grid[i][j] = 'S'
#     beacon = sensorDict[(i,j)]
#     grid[beacon[0]][beacon[1]] = 'B'

# for row in grid:
#     print(row)


# for sensor in sensorDict:
#     dist = distance(sensor,sensorDict[sensor])
#     print(dist)
#     y = sensor[0]
#     x = sensor[1]
#     for i in range(-dist, dist+1):
#         for j in range(-dist,dist+1):
#             if 0 <= y + i < n and 0 <= x + j < m:
#                 if grid[y+i][x+j] == '.' and distance(sensor,(y+i,x+j)) <= dist:
#                     grid[y+i][x+j] = '#'


# # for row in grid:
# #     print(row)
# count = 0
# for char in grid[10]:
#     if char == '#':
#         count += 1

# print(count)

