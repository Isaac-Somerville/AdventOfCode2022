with open('day7.txt') as f:
    lines = f.readlines()
    
input = []
for str in lines:
    input.append(str.strip().split(" "))
    
print(input)

class Node():
    def __init__(self, name = "", type = "", size = 0, children = {}, parent = None):
        self.name = name
        self.type = type
        self.size = size
        self.children = children
        self.parent = parent
    
root = Node(name = "/", type = "dir")
i = 1
n = len(input)

current = root
while i < n:
    if input[i][0] == "$":
        if input[i][1] == "cd":
            if input[i][2] == "..":
                current = current.parent
        
            elif input[i][2] == "/":
                current = root
    
            else:
                current = current.children[input[i][2]]
            
    elif input[i][0] == 'dir':
        if input[i][1] not in current.children:
            current.children[input[i][1]] = Node(name = input[i][1], type = "dir", size = 0, children = {}, parent = current)
    else:
        if input[i][1] not in current.children:
            current.children[input[i][1]] = Node(name = input[i][1], type = "file", size = int(input[i][0]), children = {}, parent = current)
    
    i += 1
                  

sizeDict = {}

def findSizes(root):
    for child in root.children:
        if root.children[child].type == "file":
            root.size += root.children[child].size
        else:
            root.size += findSizes(root.children[child])
    
    sizeDict[root] = root.size
    return root.size

findSizes(root)

print(sizeDict)

# count = 0
# for dir in sizeDict:
#     if sizeDict[dir] <= 100000:
#         count += sizeDict[dir]
        
# print(count)
# # 756542

for dir in sizeDict:
    if dir.name == "/":
        totalSize = sizeDict[dir]
        
print(totalSize)
# totalSize == 45174025
unusedSpace = 70000000 - totalSize
print(unusedSpace)
#unusedSpace == 24825975
requiredSpace = 30000000 - unusedSpace
print(requiredSpace)
#requiredSpace == 5174025

potentials = []
for dir in sizeDict:
    if sizeDict[dir] >= requiredSpace:
        potentials.append(sizeDict[dir])
        
print(min(potentials))