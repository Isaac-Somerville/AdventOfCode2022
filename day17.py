file = 'day17.txt'

with open(file) as f:
    lines = f.readlines()

jetLst = []
for line in lines:
    for char in line:
        jetLst.append(char)

n = len(jetLst)
print(jetLst)
print(n)
loopNum = n * 5

# tunnel = [['#'] + ['.' for _ in range(7)] + ['#'] for i in range(16)]
# tunnel[-1] = ['#' for _ in range(9)]
# for lst in tunnel:
#     print(lst)

def longRock(l,b):
    return [(b,l+i) for i in range(4)]

def plusRock(l,b):
    return [(b+2,l+1)] + [(b+1,l+i) for i in range(3)] + [(b,l+1)]

def lRock(l,b):
    return [(b+i,l+2) for i in range(3)] + [(b,l+i) for i in range(2)]

def tallRock(l,b):
    return [(b+i,l) for i in range(4)]

def squareRock(l,b):
    return [(b+i,l+j) for i in range(2) for j in range(2)]

rockDict = {0:longRock, 1:plusRock, 2:lRock, 3:tallRock, 4:squareRock}

def moveRight(rock, rockSet):
    for b, l in rock:
        if (b,l+1) in rockSet or l+1 == 8:
            return rock
    return [(b,l+1) for b,l in rock]

def moveLeft(rock,rockSet):
    for b, l in rock:
        if (b,l-1) in rockSet or l-1 == 0:
            return rock
    return [(b,l-1) for b,l in rock]

def moveDown(rock,rockSet):
    for b,l in rock:
        if (b-1,l) in rockSet or b-1 == 0:
            return rock, False
    return [(b-1,l) for b,l in rock], True


rockCount = 0
height = 0
lastHeight = 0
l = 3
jet = 0
rockSet = set()
while rockCount < 1000000000000:
    b = height + 4
    rock = rockDict[rockCount%5](l,b)
    moving = True
    while moving:
        if jetLst[jet%n] == '>':
            rock = moveRight(rock,rockSet)
        else:
            rock = moveLeft(rock,rockSet)
        
        rock, moving = moveDown(rock,rockSet)
        jet += 1

    rockSet.update(rock)
    height = max(height,max([pos[0] for pos in rock]))
    rockCount += 1
    # if rockCount % loopNum == 0:
    #if rockCount % 10000000000 == 0:
        # print(lastHeight)
        # newHeight = height - lastHeight
        # print(newHeight)
        # lastHeight = height
        # print(height % 5)
    if rockCount % 10000000000 == 0:
        print(height)
        print(rockCount//10000000000)

    
print(height)





