class Blizzard:
    def __init__(self,pos,dir):
        self.pos = pos
        self.dir = dir

    def nextPos(self,n,m):
        dirVec = {'>': (0,1), '<':(0,-1), '^':(-1,0), 'v':(1,0)}
        newPos = ((self.pos[0] + dirVec[self.dir][0]) % n , (self.pos[1] + dirVec[self.dir][1]) % m)
        self.pos = newPos
        return newPos


def makeInput(file):
    with open(file) as f:
        lines = f.readlines()
    
    grid = []
    for line in lines:
        grid.append(line.strip())

    blizList = []
    blizSet = set()
    n = len(grid)
    m = len(grid[0])
    for i in range(n):
        for j in range(m):
            if grid[i][j] != '.' and grid[i][j] != '#':
                blizSet.add((i-1,j-1))
                blizList.append(Blizzard((i-1,j-1),grid[i][j]))
    
    return grid, blizList

grid, blizList = makeInput("day24.txt")
n,m = len(grid)-2, len(grid[0])-2
start = (-1,0)
end = (n,m-1)

def findEnd(blizList, start, end, n, m):
    time = 0
    queue = [start]
    steps = [(0,1),(0,-1), (-1,0) , (1,0), (0,0)]
    while queue:
        blizSet = set()
        for bliz in blizList:
            blizSet.add(bliz.nextPos(n,m))
            #print(bliz.pos)
        
        newQueue = []
        newQueueSet = set()
        for i in range(len(queue)):
            y,x = queue[i]
            for step in steps:
                yStep, xStep = step
                if (y+yStep,x+xStep) == end:
                    print("minimum time =", time+1)
                    return blizList, time+1
                if ((y+yStep,x+xStep) == start) or (0<= y+yStep < n and 0<= x+xStep < m and (y+yStep,x+xStep) not in blizSet):
                    if (y+yStep,x+xStep) not in newQueueSet:
                        newQueue.append((y+yStep,x+xStep))
                        newQueueSet.add((y+yStep,x+xStep))
        queue = newQueue
        time += 1
        print(time)


blizList,time1 = findEnd(blizList,start,end,n,m)
blizList,time2 = findEnd(blizList,end,start,n,m)
blizList,time3 = findEnd(blizList,start,end,n,m)

print(time1)
print(time2)
print(time3)
print(time1+time2+time3)