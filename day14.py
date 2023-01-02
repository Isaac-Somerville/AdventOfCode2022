with open('day14.txt') as f:
    lines = f.readlines()

input = []
for line in lines:
    path = []
    temp = line.strip().split(' -> ')
    for pair in temp:
        tempPair = pair.split(',')
        tempLst = []
        for x in tempPair:
            tempLst.append(int(x))
        path.append(tempLst)
    input.append(path)

maxL = 0
maxD = 0
minD = 0
minL = 500
for path in input:
    for l, d in path:
        maxL = max(maxL,l)
        maxD = max(maxD,d)
        minD = min(minD,d)
        minL = min(minL,l)

newInput = []
for path in input:
    newPath = []
    for l,d in path:
        newPair = [d,l]
        newPath.append(newPair)
    newInput.append(newPath)

print(maxL,minL,maxD,minD)
matrixDims = [maxD-minD+3,1000]
sand = (0,500)
print(matrixDims,sand)
print(newInput)

grid = [['.' for j in range(matrixDims[1])] for i in range(matrixDims[0])]
grid[sand[0]][sand[1]] = '+'
grid[-1] = ['#' for _ in range(len(grid[0]))]

#print(input)

for path in newInput:
    for i in range(len(path)-1):
        x,y = path[i]
        while x != path[i+1][0]:
            grid[x][y] = '#'
            if x < path[i+1][0]:
                x += 1
            else:
                x -= 1
        while y != path[i+1][1]:
            grid[x][y] = '#'
            if y < path[i+1][1]:
                y += 1
            else:
                y -= 1
    grid[path[-1][0]][path[-1][1]] = '#'

for row in grid:
    print(row)

def sandFall(grid, start):
    n = len(grid)
    m = len(grid[0])
    moving = True
    offGrid = False
    xPos, yPos = start
    while moving and not offGrid:
        if 0 <= xPos + 1 < n: # move down, stay in grid
            if grid[xPos+1][yPos] == '.': #can move down
                xPos += 1
            
            elif 0 <= yPos-1 < m: #move diag left, stay in grid
                if grid[xPos+1][yPos-1] == '.': #can move diag left
                    xPos +=1
                    yPos -=1
                
                elif 0 <= yPos + 1 < m: #move diag right, stay in grid
                    if grid[xPos+1][yPos+1] == '.': #can move diag right
                        xPos += 1
                        yPos += 1
                    else: #cannot move
                        moving = False
                
                else:
                    offGrid = True
            else:
                offGrid = True
        else:
            offGrid = True
    
    if not (offGrid or [xPos,yPos] == start):
        grid[xPos][yPos] = 'o'
        return grid, True
    
    else:
        if offGrid:
            print('OFFGRID')
        return grid, False

#print(' ')

sandCount = 0
addSand = True
while addSand == True:
    grid, addSand = sandFall(grid, [sand[0],sand[1]])
    sandCount += 1

# for row in grid:
#     print(row)

print(sandCount)