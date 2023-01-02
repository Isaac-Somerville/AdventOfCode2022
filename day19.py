from math import ceil 

def makeInput(file):
    with open(file) as f:
        lines = f.readlines()

    inputLst = []
    for x in lines:
        line = x.strip().split('costs')
        print(line)
        i = 1
        lst = []
        while i < len(line):
            current = line[i].split('and')
            for y in current:
                j = 0
                while j < len(y) and y[j] == ' ':
                    j += 1
                temp = y[j]
                j += 1
                while j < len(y) and y[j] != ' ':
                    temp += y[j]
                    j += 1
                lst.append(int(temp))
            i += 1
        inputLst.append(lst)

    dictLst = []
    for lst in inputLst:
        costDict = {}
        i = 0 
        while i < 6:
            if i ==0:
                costDict['ore'] = {'ore':int(lst[i])} #costs ore
            if i == 1:
                costDict['clay'] = {'ore':int(lst[i])}#)costs ore
            if i == 2:
                costDict['obsidian'] = {'ore':int(lst[i]),'clay':int(lst[i+1])}#costs ore and clay
                i += 1
            if i == 4:
                costDict['geode'] = {'ore':int(lst[i]), 'obsidian':int(lst[i+1])} #costs ore and obsidian
                i += 1
            i += 1
        dictLst.append(costDict)

    return dictLst

input = makeInput('day19test.txt')
# print(input)
# for costDict in input:
#     for robot in costDict:
#         print(costDict[robot])

resources = {'geode':0, 'obsidian':0, 'clay':0, 'ore':0}
robots = {'geode':0, 'obsidian':0, 'clay':0, 'ore':1,}
time = 24

def findMaxOutput(costDict, resources, robots, time):
    # print(robots)
    # print(time)
    nextRobots = []
    if robots['obsidian'] == 0:
        if robots['clay'] == 0:
            nextRobots.append('clay')
            if robots['ore'] < maxResourceDict['ore']:
                nextRobots.append('ore')
        else:
            nextRobots.append('obsidian')
            if robots['clay'] < maxResourceDict['clay']:
                nextRobots.append('clay')
            if robots['ore'] < maxResourceDict['ore']:
                nextRobots.append('ore')
    else:
        nextRobots.append('geode')
        if robots['obsidian'] < maxResourceDict['obsidian']:
            nextRobots.append('obsidian')
        if robots['clay'] < maxResourceDict['clay']:
            nextRobots.append('clay')
        if robots['ore'] < maxResourceDict['ore']:
            nextRobots.append('ore')

    if nextRobots:
        geodeLst = []
        for nextRobot in nextRobots:
            # resource + minutes * robots >= costDict[robot][resource]
            # => minutes >= (costDict[robot][resource] - resources[resource]) / robots[robot]
            maxMinsNeeded = 0
            for resource in costDict[nextRobot]:
                minsNeeded = ceil((costDict[nextRobot][resource] - resources[resource] )/ robots[resource])
                maxMinsNeeded = max(maxMinsNeeded, minsNeeded)
            maxMinsNeeded += 1
            print(time, nextRobot, maxMinsNeeded)
            if maxMinsNeeded < time:
                tempResources = resources.copy()
                tempRobots = robots.copy()
                for resource in costDict[nextRobot]:
                    tempResources[resource] += (tempRobots[resource] * (maxMinsNeeded) - costDict[nextRobot][resource])
                tempRobots[nextRobot] += 1
                geodeLst.append(findMaxOutput(costDict,tempResources, tempRobots, time - maxMinsNeeded))
        if geodeLst:
            print(robots)
            return max(geodeLst)
        else:
            print(robots)  
            return robots['geode'] * time

    else: 
        print(robots)
        return robots['geode'] * time

# for costDict in input:
costDict = input[0]
maxResourceDict = {}
for resource in resources:
    maxResource = 0
    for robot in costDict:
        if resource in costDict[robot]:
            maxResource = max(maxResource, costDict[robot][resource])
    maxResourceDict[resource] = maxResource


print(maxResourceDict)
resources = {'geode':0, 'obsidian':0, 'clay':0, 'ore':0}
robots = {'geode':0, 'obsidian':0, 'clay':0, 'ore':1}
canBuildDict = {'geode':False, 'obsidian':False, 'clay':False, 'ore':False}
time = 24

print(findMaxOutput(costDict,resources,robots,time))

#     if time > 0 :
#         geodeLst = []
#         for robot in canBuildDict:
#             if canBuildDict[robot] == True:
#                 canBuildDict[robot] = False
#                 tempResources = resources.copy()
#                 tempRobots = robots.copy()
#                 tempCanBuildDict = canBuildDict.copy()
#                 otherTempResources = resources.copy()
#                 otherTempRobots = robots.copy()
#                 otherTempCanBuildDict = canBuildDict.copy()
#                 tempRobots[robot] += 1
#                 for resource in costDict[robot]:
#                     tempResources[resource] -= costDict[robot][resource]
#                 geodeLst.append(findMaxOutput(costDict, tempResources, tempRobots, time - 1, tempCanBuildDict))
#                 geodeLst.append(findMaxOutput(costDict, otherTempResources, otherTempRobots, time -1 , otherTempCanBuildDict))
#         if geodeLst:
#             return max(geodeLst)
#         else:
#             return findMaxOutput(costDict, resources, robots, time -1 , canBuildDict)

#     else:
#         print("robots=", robots)
#         #print("resources=", resources)
#         return resources['geode']
   

