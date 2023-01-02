from math import inf

file = 'day22.txt'

def makeInput(file):
    with open(file) as f:
        lines = f.readlines()
    
    tempGrid = []
    maxLength = 0
    minLength = inf
    for i in range(len(lines)-2):
        line = list(lines[i][:-1])
        maxLength = max(maxLength,len(line))
        minLength = min(minLength,len(line))
        tempGrid.append(line)
    
    grid = []
    for line in tempGrid:
        if len(line) < maxLength:
            grid.append(line + [' ' for _ in range(maxLength - len(line))])
        else:
            grid.append(line)
    
    for line in grid:
        if len(line) != maxLength:
            print(False)
        # print(line)

    line = lines[-1]
    inst = []
    temp = ''
    for i in range(len(line)):
        if line[i] == 'R' or line[i] == 'L':
            if temp:
                inst.append(int(temp))
                inst.append(line[i])
                temp = ''
            else:
                inst.append(line[i])
        elif temp:
            temp += line[i]
        else:
            temp = line[i]
        
    if temp:
        inst.append(int(temp))
        
    return grid, inst

grid, insts = makeInput(file)
# print(sideLength)
# print(len(grid))
# print(len(grid[0]))
top = [grid[i][50:100] for i in range(50)]
right = [grid[i][100:150] for i in range(50)]
front = [grid[i][50:100] for i in range(50,100)]
bottom = [grid[i][50:100] for i in range(100,150)]
left = [grid[i][0:50] for i in range(100,150)]
back = [grid[i][0:50] for i in range(150,200)]

# sides = [top,right,front,bottom,left,back]
# for side in sides:
#     for row in side:
#         for elem in row:
#             if not (elem == '.' or elem == '#'):
#                 print('Found blank')

# dirs = [0:'U', 1:'R', 2:'D', 3:'L']
dirDict = {0:[-1,0], 1:[0,1], 2:[1,0], 3:[0,-1]}
y = 0
x = 0
dir = 1

def topFunc(dir,y,x):
    if dir == 0:
        return ('back', 1, (x,0))
    elif dir == 1: 
        return ('right', 1, (y,0))
    elif dir == 2: 
        return ('front', 2, (0,x))
    elif dir == 3: 
        return ('left', 1, (49-y,0))

def leftFunc(dir,y,x):
    if dir == 0:
        return ('front',1,(x,0))
    elif dir == 1:
        return ('bottom',1,(y,0))
    elif dir == 2:
        return ('back',2,(0,x))
    elif dir == 3:
        return ('top',1,(49-y,0))
    
def rightFunc(dir,y,x):
    if dir == 0: 
        return ('back', 0, (49,x))
    elif dir == 1: 
        return ('bottom', 3, (49-y,49))
    elif dir == 2: 
        return ('front', 3, (x,49))
    elif dir == 3: 
        return ('top', 3, (y,49))


def bottomFunc(dir,y,x):
    if dir == 0:
        return ('front',0,(49,x))
    elif dir == 1:
        return ('right',3,(49-y,49))
    elif dir == 2:
        return ('back',3,(x,49))
    elif dir == 3:
        return ('left',3,(y,49))

def frontFunc(dir,y,x):
    if dir == 0 :
        return ('top',0,(49,x))
    elif dir == 1:
        return ('right',0,(49,y))
    elif dir == 2:
        return ('bottom',2,(0,x))
    elif dir == 3:
        return ('left',2,(0,y))

def backFunc(dir,y,x):
    if dir == 0:
        return ('left',0,(49,x))
    elif dir == 1:
        return ('bottom',0,(49,y))
    elif dir == 2:
        return ('right',2,(0,x))
    elif dir == 3:
        return ('top',2,(0,y))

funcDict = {'top': topFunc,
            'right' : rightFunc,
            'front': frontFunc,
            'bottom' : bottomFunc,
            'left' : leftFunc,
            'back' : backFunc
            }

sideDict = {'top': top,
            'right' : right,
            'front': front,
            'bottom' : bottom,
            'left' : left,
            'back' : back
            }


def changeDir(turn,dir):
    if turn == 'L':
        dir = (dir - 1) % 4
    else:
        dir = (dir + 1) % 4
    return dir

def move(side,y,x,dir,dirDict,dist,funcDict,sideDict):
    grid = sideDict[side]
    vec = dirDict[dir]
    yNext, xNext = (y + vec[0]), (x + vec[1])
    while 0 <= yNext < 50 and 0 <= xNext < 50 and grid[yNext][xNext] == '.' and dist > 0:
        y, x = yNext, xNext
        #print(y,x)
        yNext, xNext = (y + vec[0]), (x + vec[1])
        dist -= 1
    
    if dist == 0 or (0 <= yNext < 50 and 0 <= xNext < 50 and grid[yNext][xNext] == '#'): # can no longer move
        return side,y,x,dir
    
    else: #reached edge of side, find next side
        nextFunc = funcDict[side]
        nextSide, nextDir, (yNext,xNext) = nextFunc(dir,y,x)
        print(side,dir,y,x)
        print(nextSide, nextDir, yNext, xNext)
        nextGrid = sideDict[nextSide]

    if nextGrid[yNext][xNext] == '#': #can't move onto next side
        return side,y,x,dir

    else: # can move onto next side
        return move(nextSide,yNext,xNext,nextDir,dirDict,dist-1,funcDict,sideDict)

def findEnd(side,insts,y,x,dir,dirDict,funcDict,sideDict):
    for inst in insts:
        # print(side,y,x,dir)
        # print(inst)
        if type(inst) == int:
            side,y,x,dir = move(side,y,x,dir,dirDict,inst,funcDict,sideDict)
        else:
            dir = changeDir(inst,dir)
    return side,y,x,dir

# dirs = [0:'U', 1:'R', 2:'D', 3:'L']
dirDict = {0:[-1,0], 1:[0,1], 2:[1,0], 3:[0,-1]}
y = 0
x = 0
side = 'top'
dir = 1
print(findEnd(side,insts,0,0,1,dirDict,funcDict,sideDict))

print((1000*(100+14+1)) + (4*(50+26+1)) + 3)
# 110176 too low
# 115111 too low (change 100 and 0 for bottom!)

# print(len(top),len(top[0]))
# print(len(right),len(right[0]))
# print(len(front),len(front[0]))
# print(len(bottom),len(bottom[0]))
# print(len(left),len(left[0]))
# print(len(back),len(back[0]))
# print(top)
# print(right)
# print(front)
# print(bottom)
# print(left)
# print(back)
# for line in grid:
#     print(line)
# print(insts)


# def changeDir(turn,dir):
#     if turn == 'L':
#         dir = (dir - 1) % 4
#     else:
#         dir = (dir + 1) % 4
#     return dir

# def move(grid,y,x,vec,dist):
#     n = len(grid)
#     m = len(grid[0])
#     yNext, xNext = (y + vec[0]) % n , (x + vec[1]) % m
#     while 0 <= yNext < n and 0 <= xNext < m and grid[yNext][xNext] == '.' and dist > 0:
#         y, x = yNext, xNext
#         #print(y,x)
#         yNext, xNext = (y + vec[0]) % n , (x + vec[1]) % m
#         dist -= 1
    
#     if dist == 0 or grid[yNext][xNext] == '#':
#         return y,x
    
#     while grid[yNext][xNext] == ' ':
#         yNext, xNext = (yNext + vec[0]) % n , (xNext + vec[1]) % m
    
#     if grid[yNext][xNext] == '#':
#         return y,x
    
#     y, x = yNext, xNext
#     #print(y,x)
#     dist -= 1
#     return move(grid,y,x,vec,dist)

# def findEnd(grid,insts,y,x,dir, dirDict):
#     vec = dirDict[dir]
#     for inst in insts:
#         if type(inst) == int:
#             y,x = move(grid,y,x,vec,inst)
#         else:
#             dir = changeDir(inst,dir)
#             vec = dirDict[dir]
#     return y,x,dir


# y,x,dir = findEnd(grid,insts,y,x,dir,dirDict)
# print(1000*(y+1) + 4*(x+1))
# print(dir)