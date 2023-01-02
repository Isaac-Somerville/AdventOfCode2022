class Valve:
    def __init__(self, name = '', flow = 0, adjacents = [], closed = True):
        self.name = name
        self.flow = flow
        self.adjacents = adjacents
        self.closed = closed

def makeInput(file):
    tunnelDict = {}
    tempDict = {}
    adjDict = {}
    with open(file) as f:
        lines = f.readlines()
    for x in lines:
        line = x.strip()
        valve = Valve(name = line[6:8], flow = 0, adjacents = [], closed = True)

        if valve.name == 'AA':
            current = valve
               
        i = 9
        while line[i] != '=':
            i += 1
        i += 1

        temp = line[i]
        i += 1
        while line[i] != ';':
            temp += line[i]
            i += 1
        valve.flow = int(temp)
        if valve.flow == 0:
            valve.closed = False

        while i < len(line):
            while not line[i].isupper():
                i += 1
            temp = line[i]
            i += 1
            while i < len(line) and line[i].isupper():
                temp += line[i]
                i += 1
            valve.adjacents.append(temp)
    
        tunnelDict[valve] = []
        tempDict[valve.name] = valve
        adjDict[valve] = valve.adjacents

    for valve in tunnelDict:
        for adj in adjDict[valve]:
            tunnelDict[valve].append(tempDict[adj])

    return tunnelDict,tempDict, current

tunnelDict, tempDict, current = makeInput('day16.txt')
# for valve in tunnelDict:
#     print(valve.name)
#     print(tunnelDict[valve])
        
# def findMaxPressure(current, currentPressure, totalPressure, time):
#     queue = [current]
#     visited = {current}
#     distance = 1
#     nextLst = []
#     while queue:
#         newQueue = []
#         if time - distance > 1:
#             for i in range(len(queue)):
#                 current = queue[i]
#                 for adj in tunnelDict[current]:
#                     if adj not in visited:
#                         if adj.closed == True:
#                             nextLst.append([adj, distance])
#                         visited.add(adj)
#                         newQueue.append(adj)
#         queue = newQueue
#         distance += 1
#     if nextLst:
#         lst = []
#         for adj, newTime in nextLst:
#             adj.closed = False
#             newPressure = findMaxPressure(adj, currentPressure + adj.flow, 
#                 totalPressure + (newTime+1) * currentPressure, time - newTime -1)
#             adj.closed = True
#             lst.append(newPressure)
#         x = max(lst)
#         idx = lst.index(x)
#         correctValve = nextLst[idx][0].name
#         print(correctValve)
#         return x
    
#     return totalPressure + currentPressure * time

def findMaxPressure(me ,elephant,meTime, eleTime, pressure, totalPressure, time):
    if me == None:
        while eleTime != 0:
            eleTime -= 1
            time -= 1
            totalPressure += pressure

    elif elephant == None:
        while meTime != 0:
            meTime -= 1
            time -= 1
            totalPressure += pressure
    
    else:
        while meTime != 0 and eleTime != 0:
            meTime -= 1
            eleTime -= 1
            time -= 1
            totalPressure += pressure

    if me != None and meTime == 0:
        pressure += me.flow
        queue = [me]
        meVisited = {me}
        distance = 2
        nextLst = []
        while queue:
            newQueue = []
            if time - distance > 0:
                for i in range(len(queue)):
                    current = queue[i]
                    for adj in tunnelDict[current]:
                        if adj not in meVisited:
                            if adj.closed == True:
                                nextLst.append([adj, distance])
                            meVisited.add(adj)
                            newQueue.append(adj)
            queue = newQueue
            distance += 1
        if nextLst:
            lst = []
            for adj, newTime in nextLst:
                adj.closed = False
                #print(elephant.name)
                newPressure = findMaxPressure(adj, elephant, newTime, eleTime, 
                                pressure, totalPressure, time)
                #print(elephant.name)
                adj.closed = True
                lst.append(newPressure)
            x = max(lst)
            # idx = lst.index(x)
            # correctValve = nextLst[idx][0].name
            # print(correctValve)
            #print(me.name, elephant.name, time)
            return x
        else:
            me = None

    if me == None:
        while eleTime != 0:
            eleTime -= 1
            time -= 1
            totalPressure += pressure

    if elephant != None and eleTime == 0:
        pressure += elephant.flow
        queue = [elephant]
        eleVisited = {elephant}
        distance = 2
        nextLst = []
        while queue:
            newQueue = []
            if time - distance > 0:
                for i in range(len(queue)):
                    current = queue[i]
                    for adj in tunnelDict[current]:
                        if adj not in eleVisited:
                            if adj.closed == True:
                                nextLst.append([adj, distance])
                            eleVisited.add(adj)
                            newQueue.append(adj)
            queue = newQueue
            distance += 1
        if nextLst:
            lst = []
            for adj, newTime in nextLst:
                adj.closed = False
                newPressure = findMaxPressure(me, adj, meTime, newTime, 
                                pressure, totalPressure, time)
                adj.closed = True
                lst.append(newPressure)
            x = max(lst)
            # idx = lst.index(x)
            # correctValve = nextLst[idx][0].name
            # print(correctValve)
            #print(me.name, elephant.name, time)
            return x
        else:
            elephant = None

    if elephant == None and me != None:
        return findMaxPressure(me, elephant, meTime, eleTime, pressure,
                            totalPressure,time)

    #print(pressure)
    return totalPressure + pressure * time




print(findMaxPressure(current, current, 0, 0, 0, 0, 26))

#not 2907 (too high)